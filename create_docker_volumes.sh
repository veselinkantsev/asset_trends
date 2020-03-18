#!/bin/bash

for II in prometheus grafana;do

  # Create volume
  docker volume create ${II}_data

  # Copy files to volume
  docker run \
    --rm \
    -v $PWD/conf:/_bind_mount:ro \
    -v ${II}_data:/_volume \
    --entrypoint=/bin/sh \
    alpine \
    -c "mkdir /_volume/${II} && cp /_bind_mount/${II}.* /_volume/${II}/ && chmod 777 /_volume/${II} && chmod 666 /_volume/${II}/*"

done
