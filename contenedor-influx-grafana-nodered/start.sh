#!/bin/bash
set -e

echo "Creating API token..."

TOKEN=$(influx auth create \
  --org "somorrostro" \
  --description "Read-write token" \
  --read-buckets \
  --write-buckets \
  --token my-super-secret-admin-token \
  --json | awk -F'"' '/"token":/{print $4}')

if [ -n "$TOKEN" ]; then
    echo "$TOKEN" > /shared/api-token.txt
    echo "Token saved successfully"
else
    echo "Error: Failed to create token"
    exit 1
fi