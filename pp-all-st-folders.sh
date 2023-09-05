#!/usr/bin/env bash

# Print some info
echo "The script you are running has:"
echo "name     : [$(basename "$0")]"
echo "location : [$(dirname "$0")]"
echo "pwd      : [$(pwd)]"

for d in */ ; do
    (cd $d; bash $(dirname "$0")/pp-spacetime.sh)
done

