#!/usr/bin/env bash
#simple if

if [ $1 -gt 100 ]
then
  echo "Greater than 100"
elif [ $1 -lt 100 ]
then
  echo "Less than 100"
fi
