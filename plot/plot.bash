#!/bin/bash

# /home/ann/pd101/plot/plot.bash

# This script should help me visualize predictions.

mkdir -p /tmp/pd101/
cd       /tmp/pd101/
echo /home/ann/pd101/plot/wgetem.bash

# Now I should have new CSV files in /tmp/pd101/

set -x
# I should create wide1.csv
sqlite3 pd101.db '.read /home/ann/pd101/plot/joinem.sql'
