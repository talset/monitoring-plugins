#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Florian Lambert <flambert@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Requirments: python, lvm2-python-libs

import sys
import argparse
import subprocess
import re

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

STATE_TEXT = ['Ok', 'Warning', 'Critical', 'Unknow']

STATE = STATE_OK


PARSER = argparse.ArgumentParser(description='Check lvm usage.')
PARSER.add_argument("-vg", "--vgname", type=str,
                    required=True,
                    help='vg name of the lv (ex : docker-vg)')
PARSER.add_argument("-lv", "--lvname", type=str,
                    required=True,
                    help='lv name to check (ex : docker-pool)')
PARSER.add_argument("-w", "--warning", type=str,
                    required=False,
                    help='Warning Percentage (Default : 80)',
                    default=80)
PARSER.add_argument("-c", "--critical", type=str,
                    required=False,
                    help='Critical Percentage (Default : 90)',
                    default=90)
ARGS = PARSER.parse_args()

def compare(value,wlimit,climit):
   global STATE
   if float(value) >= float(climit):
      if STATE < STATE_CRITICAL:
         STATE = STATE_CRITICAL
   elif float(value) >= float(wlimit):
      if STATE < STATE_WARNING:
         STATE = STATE_WARNING

if __name__ == "__main__":
   if ARGS.lvname and ARGS.vgname:
      cmd="/sbin/lvs --noheadings -o data_percent,metadata_percent --separator '-' %s/%s" % (ARGS.vgname,ARGS.lvname)
      stdout = subprocess.check_output(cmd, shell=True)
      (lvdata,lvmeta) = re.split('-', stdout.strip().replace(',','.'))
      #check meta
      compare(lvmeta,ARGS.warning,ARGS.critical)
      #check data
      compare(lvdata,ARGS.warning,ARGS.critical)
      
   print "%s: %s/%s - data(%s%%) meta(%s%%)" % (STATE_TEXT[STATE], ARGS.vgname, ARGS.lvname, lvdata, lvmeta)
   sys.exit(STATE)
