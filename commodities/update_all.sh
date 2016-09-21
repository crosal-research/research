#!/bin/bash
######################################################################
# script to update input/output of the commodity pipeline
# initial date: 13/09/2016
######################################################################

caminho="/home/jmrosal/Documents/crosal/research/research/data/scripts/"
file="imf_commodity.py"

if [ -f $caminho$file ]; then
    echo "retrieving commodity information..."
    python "$caminho$file"
    echo "...updated finished"
else
    echo "file $caminho$file not found"
    exit 1
fi

if [ -f ./commodities_real.py ]; then
    echo "producing chart..."
    python "./commodities_real.py"
    echo "...chart produced"
else
    echo "file $file not found"
    exit 1
fi
