#!/usr/bin/env bash
#search for files in a directory and displaying their contents

files=$* #string of all arguments

for file in $files
do
  if [ -e $file ]
  then
    echo "$file present in directory"
    echo "Printing the contents of $file"
    more $file
  else echo "$file not found"
  fi
done
