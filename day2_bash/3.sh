#!/usr/bin/env bash
#passing arguments

echo "Number of arguments passed: $#"
echo "Script name: $0"

echo "$1 has been copied to $2"
cp -R $1 $2

echo "$@"
ls
