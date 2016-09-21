######################################################################
# updates script related to credit markets
# initial date: 12/09/2016
######################################################################

caminho="../data/scripts/"

files="gdp_categories.py gdp_sa_categories.py ibc_br.py nuci_bz.py retail_activities_sa.py industry_sa.py brazil_services.py confidence.py"

#update files
echo "Updating all activity files for Brazil"

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
