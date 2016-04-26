## monitoring-plugins
Check compatible with Sensu, nagios ...

##network/check_arp_incomplete.sh

Check if we have some incomplete ARP

Script help

```bash
check_arp_incomplete.sh 1.0 (c) 2015 Florian Lambert (flambert@redhat.com)

Usage: check_arp_incomplete.sh -i

-h Show this page
-v Script version
-i --incomplete check if we have incomplete ARP
```

Script exemples

```bash
bash check_arp_incomplete.sh -i
ARP OK : 0 incomplete

bash check_arp_incomplete.sh -i
CRITICAL OK : 3 incomplete
```
