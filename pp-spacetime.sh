#!/usr/bin/env bash

# Input
VISITDIR=~/prog/visit-knotmapgh/

# Print some info
echo "The script you are running has:"
echo "name     : [$(basename "$0")]"
echo "location : [$(dirname "$0")]"
echo "pwd      : [$(pwd)]"

python3 $(dirname "$0")/pp-plot-residual.py
python3 $(dirname "$0")/pp-plot-st-forces.py
$VISITDIR/bin/visit -cli -no-vis -nowin -s $(dirname "$0")/pp-slice-st-sol-zoom.py
bash $(dirname "$0")/create-u-v-fig.sh
bash $(dirname "$0")/create-u-v-p-fig.sh
