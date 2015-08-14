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
# Requirments: python

import sys
import argparse

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
ARGS = PARSER.parse_args()

class Lvmcheck(object):
  def __init__(self):
    print 'bla'

  def findlv(self):
    print 'lvs'

if __name__ == "__main__":

   lvmcheck = Lvmcheck()

   if ARGS.lvname and ARGS.vgname:
      print findlv()

   print "%s: %s/%s" % (STATE_TEXT[STATE], ARGS.vgname, ARGS.lvname)
   sys.exit(STATE)
