# Containerizable (using docker) complex of three CNNs (using mxnet) with API (using Flask)

## Build
    docker build -t new_image .

## Run
    docker run -it --rm -d -p 8080:80 --name 3net_mnist new_image