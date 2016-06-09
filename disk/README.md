## monitoring-plugins
Check compatible with Sensu, nagios ...

##disk/check_disk.py

Parse the output of df command and check the disk and inode usage of each mounted volumes

Script help

```bash
python check_disk.py -h
usage: check_disk.py [-h] [-b BASE] [-e EXCLUDES [EXCLUDES ...]] [-w WARNING]
                     [-c CRITICAL] [-v]

Disk check recurcive

optional arguments:
  -h, --help            show this help message and exit
  -b BASE, --base BASE  base directory to monitor. For example if you want to
                        monitor only volume mounted under /host/ (Default: /)
  -e EXCLUDES [EXCLUDES ...], --excludes EXCLUDES [EXCLUDES ...]
                        List of mountpoint to recurcively exclude ex:
                        /var/lib/origin /var/lib/docker
  -w WARNING, --warning WARNING
                        Warning value (Default: 85)
  -c CRITICAL, --critical CRITICAL
                        Critical value (Default: 95)
  -v, --version         Print script version
```
