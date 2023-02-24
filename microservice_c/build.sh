#!/bin/bash

set -xe
SERVICE_NAME=$( echo "$PWD" | awk -F '/' '{print $NF}')

docker build \
  --file Dockerfile \
  -t "${1}/${SERVICE_NAME}:${2}" \
  -t "${1}/${SERVICE_NAME}:latest" \
  .
