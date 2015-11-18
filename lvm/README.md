## monitoring-plugins
Check compatible with Sensu, nagios ...


##lvm/check_lvm_usage.py

Check logical volume Data an Meta % with lvs commande.
```bash
lvs
  LV          VG        Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  docker-pool docker-vg twi-aot--- 51,78g             58,53  6,76
```

Script help

```bash
usage: check_lvm_usage.py [-h] -vg VGNAME -lv LVNAME [-w WARNING]
                          [-c CRITICAL]

Check lvm usage.

optional arguments:
  -h, --help            show this help message and exit
  -vg VGNAME, --vgname VGNAME
                        vg name of the lv (ex : docker-vg)
  -lv LVNAME, --lvname LVNAME
                        lv name to check (ex : docker-pool)
  -w WARNING, --warning WARNING
                        Warning Percentage (Default : 80)
  -c CRITICAL, --critical CRITICAL
                        Critical Percentage (Default : 90)
```

Script exemples

```bash
python check_lvm_usage.py -vg docker-vg -lv docker-pool 
Ok: docker-vg/docker-pool - data(58.69%) meta(6.94%)

python check_lvm_usage.py -vg docker-vg -lv docker-pool --warning 20 --critical 50
Critical: docker-vg/docker-pool - data(58.66%) meta(6.90%)
```
