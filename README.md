# ton-metrics

## How to Run
```
docker run -d \
    --network=host \
    --name=ton-metrics \
    -e FLASK_PORT=5000 \
    -e ENDPOINT=http://127.0.0.1 \
    jionederfull/ton-metrics:0.3
```

## Basic Test
```
curl localhost:5000/metrics
```





```
docker build --platform linux/amd64 -t jionederfull/ton-metrics:0.3 ./
```
```
docker push jionederfull/ton-metrics:0.3
```
