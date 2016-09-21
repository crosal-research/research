#!/bin/bash
######################################################################
# script to fetch data and update output of international data
# initial date: 14/09/2016
######################################################################

echo "Initiating script to update international files..."

caminho="$HOME/Documents/crosal/research/research/data/scripts/"

echo $caminho

files="interest_spread.py mon_policy_map.py"

#update files
echo "retriving data..."

for file in $files; do
    if [ -f  $caminho$file ]; then
        echo "updating data from $file..."
        python "$caminho$file"
        echo "$file done!..."
    else
        echo "$caminho$file not found. Exiting process."
        exit 1
    fi
done

echo "data retrieved. Updating Outcome files..."

for file in $(ls | grep py); do
    if [ -f $file ]; then
        echo "Updating output of file $file"
        python "$file"
        echo "Update done!"
    else
        echo "File $file not found. Aborting the process."
        exit 1
    fi
done

echo "Full update finished!"
