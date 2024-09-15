#!/usr/bin/env bash

# Input
VISITDIR=~/prog/visit-par-knotedge/

# Print some info
echo "The script you are running has:"
echo "name     : [$(basename "$0")]"
echo "location : [$(dirname "$0")]"
echo "pwd      : [$(pwd)]"

$VISITDIR/bin/visit -cli  -s $(dirname "$0")/pp-slice-st-residual.py

