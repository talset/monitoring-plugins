## monitoring-plugins
Check compatible with Sensu, nagios ...

##network/check_arp_incomplet.sh

Check if we have some incomplet ARP

Script help

```bash
check_arp_incomplet.sh 1.0 (c) 2015 Florian Lambert (flambert@redhat.com)

Usage: check_arp_incomplet.sh -i

-h Show this page
-v Script version
-i --incomplet check if we have incomplet ARP
```

Script exemples

```bash
bash check_arp_incomplet.sh -i
ARP OK : 0 incomplet

bash check_arp_incomplet.sh -i
CRITICAL OK : 3 incomplet
```
