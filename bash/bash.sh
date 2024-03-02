## read file line by line
while IFS= read -r line; do
  echo "$line"
done < file.txt

## find and replace
sed -i 's/old-text/new-text/g' file.txt

## ls and find with grep
ls | grep "pattern"
