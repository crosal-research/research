#####################################################################
# updates script related to Bz cpi analises
# initial date: 12/09/2016
######################################################################

caminho="../data/scripts/"


for file in "cpi_core_bz.py" "igpm.py"; do
    if [ -f $caminho$file ]; then
        echo "updating file $file..."
        python "$caminho$file"
        echo "...$file updated"
    else
        echo "file $caminho$file not found"
        exit 1
    fi
done

for file in $(ls . | grep .py); do
    if [ -f $file  ]; then
        echo "loading file $file"
        python "$file"
        echo "$file successfully loaded"
    else
        echo "file $file not found"
        exit 1
    fi
done

echo "updating successfully completed!"
exit 0
