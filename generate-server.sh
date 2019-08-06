#!/usr/bin/env bash
dir=${PWD}

docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.0.0 \
     generate  \
     -i /local/openapi.yaml \
     -g python-flask  \
     -o /local/server/ \
     --git-repo-id wings-api \
     --git-user-id KnowledgeCaptureAndDiscovery \
     --ignore-file-override /local/.openapi-generator-ignore
