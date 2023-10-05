# base-metrics

## How to Run
```
docker run -d \
    --network=host \
    --name=base-metrics \
    -e FLASK_PORT=5000 \
    -e ENDPOINT=http://127.0.0.1:8545 \
    jionederfull/base-metrics:0.1
```

## Basic Test
```
curl localhost:5000/metrics
```





```
docker build --platform linux/amd64 -t jionederfull/base-metrics:0.1 ./
```
```
docker push jionederfull/base-metrics:0.1
```
