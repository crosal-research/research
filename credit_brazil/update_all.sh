######################################################################
# updates script related to credit markets
# initial date: 12/09/2016
######################################################################

caminho="../data/scripts/"


for file in "credit_quality.py" "credit_volume.py"; do
    if [ -f $caminho$file ]; then
        echo "updating file $file..."
        python "$caminho$file"
        echo "...$file updated"
    else
        echo "file $file not found"
        exit 1
    fi
done

for file in $(ls . | grep .py); do
    if [ -f $file  ]; then
        echo "loading file "
        python "$file"
        echo "$file successfully loaded"
    else
        echo "file $file not found"
        exit
    fi
done

echo "updating successfully completed!"
exit 0
