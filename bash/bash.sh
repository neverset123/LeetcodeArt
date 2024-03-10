# exit script if command fails
set -o errexit
# treat unset variables as an error
set -o nounset
 # set exit code to last failed command
set -o pipefail

## read file line by line
while IFS= read -r line; do
  echo "$line"
done < file.txt

## find and replace
sed -i 's/old-text/new-text/g' file.txt

## ls and find with grep
ls | grep "pattern"

## awk
awk -F ',' '{ sum += $3; count++ } END { print sum / count }' data.csv