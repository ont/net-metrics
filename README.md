# net-metrics
This docker container provides json metrics ouput for https://github.com/influxdata/telegraf collector.

## How to run
```
docker run \
    -d --name=net-metrics \
    --net=host \
    --privileged \
    -p 9000:9000 \
    ontrif/net-metrics
```

Then get metrics with:
```
curl 'localhost:9000/hooks/conns_historgram?port=443'
...
[{"hosts": 3573, "pconns": 2}, {"hosts": 2, "pconns": 9}, {"hosts": 3102, "pconns": 1}]
```
