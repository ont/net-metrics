# net-metrics
This docker container provides json metrics ouput for https://github.com/influxdata/telegraf collector.

## How to run
```
docker run \
    -d --name=net-metrics \
    --net=host \
    -p 9000:9000
    ontrif/net-metrics
```
