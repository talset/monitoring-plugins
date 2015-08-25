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
##openshift/check_openshift.py

Use token to request openshift api (/api/v1beta3/)  with Oauth.
If you didn't have token, use user/pass to perform an "oc login" and get a token.

2 checks are available
  * check_nodes : Request status of nodes through openshift API
  * check_pods : Request status of pods (with deployconfig : docker-registry and router)

Script help

```bash
python check_openshift.py -h
usage: check_openshift.py [-h] [-proto PROTOCOL] [-H HOST] [-P PORT]
                          [-u USERNAME] [-p PASSWORD] [-t TOKEN]
                          [--check_nodes] [--check_pods]

Openshift check pods

optional arguments:
  -h, --help            show this help message and exit
  -proto PROTOCOL, --protocol PROTOCOL
                        Protocol openshift (Default : https)
  -H HOST, --host HOST  Host openshift (Default : 127.0.0.1)
  -P PORT, --port PORT  Port openshift (Default : 8443)
  -u USERNAME, --username USERNAME
                        Username openshift (ex : sensu)
  -p PASSWORD, --password PASSWORD
                        Password openshift
  -t TOKEN, --token TOKEN
                        Token openshift (use token or user/pass
  --check_nodes         Check status of nodes
  --check_pods          Check status of pods ose-haproxy-router and ose-
                        docker-registry
```

We suggest to use a permanant token from a ServiceAccount. Exemple on how create one


```bash
echo '{
  "apiVersion": "v1",
  "kind": "ServiceAccount",
  "metadata": {
    "name": "metrics"
  }
}' > metricsSA.json
 
oc create -f metricsSA.json

oc describe serviceaccount metrics
oc describe secret metrics-token-bsd4v
```
