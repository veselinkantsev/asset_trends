#!/bin/bash

for II in prometheus grafana;do

  # Create volumes
  docker volume create ${II}_data

  # Put config/data files in place
  docker run \
    --rm \
    -v $PWD/conf:/conf:ro \
    -v ${II}_data:/data \
    --entrypoint=/bin/sh \
    alpine \
    -c "mkdir /data/${II} && cp /conf/${II}.* /data/${II}/ && chmod 777 /data/${II} && chmod 666 /data/${II}/*"

done
