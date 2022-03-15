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

The containers are (can be) started using **docker-compose** and are thus configured in the **docker-compose.yml** file. It defines the docker volumes (mount points/shares) and these need to be edited depending on host system. If the host sports SELinux, the volume definitions must end with **:Z** so that SELinux does not block permissions.

In **docker-compose.yml** environment variables can be added to the respective containers.

## Configure the nginx server for https

In **nginx/conf/proxy.conf** edit the two(!!) occurencies of //set $host_addr XXX;// so that //$host_addr// is set to the curren host IP or hostname.
