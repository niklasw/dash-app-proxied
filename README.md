# dash-app-proxied

Example python dash app behind nginx reverse proxy (docker/podman). It runs using two or three docker containers:

1. a custom python container that runs the app
2. an nginx container from docker hub (or similar)
3. Optional, for signed certificates, a certbot container that manages ssl certificates from letsencrypt

The containers mounts volumes from the host, so python code and configuration is persistent (and edited on the host).

Start by cloning this repository on the host.

## Build the container image

The **build-docker-image.sh** is just a single line script. Here the image name
is defined. To create the docker image, simply run the script on the host:

        ./build-docker-image.sh

## Configure the docker containers

The containers are (can be) started using **docker-compose** and are thus configured in the **docker-compose.yml** file. It defines the docker volumes (mount points/shares) and these need to be edited depending on host system. If the host sports SELinux, the volume definitions must end with **:Z** so that SELinux does not block permissions. On other systems instead append **:ro** or **:rw** as appropriate (read-only, read-write).

In **docker-compose.yml** environment variables can be added to the respective containers.

Assert that the dash service image name is the same that was set in the **build-docker-image.sh** script.

## Configure the nginx server for https

In **nginx/conf/proxy.conf** edit the two (one in each server block) occurencies of **set $host_addr XXX;** so that **$host_addr** is set to the curren host IP or hostname. The proxy parameters in the https server block are yet experimental.

Also, add certificate files (certificate.pem, key.pem) to the **certbot/certs** folder. See the readme there, on how to generate self-signed certificates, if letsencrypt/certbot is not an option.

## Editing the python app

The python application is found in the **./app/app.py** and should be edited on the host. Note the **debug** mode set in app.py and also the *FLASK_ENV=development* that can be changed in **docker-compose.yml**.

## Launching the application

The following command starts and stops all containers defined in **docker-compose.yml**.

        docker-compose up -d
        docker-compose down

View which containers are running and forcefully delete unwanted:

        docker ps                   # list running conainers
        docker ps -a                # also include stopped containers
        docker rm <container name>  # remove containers

Log in to a running container, e.g. the nginx server:

        docker exec -it nginx nxinx-proxy bash

## Access the running application

In the web broser: **https://host_addr/**
