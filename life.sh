#!/bin/bash

declare -a Files=( "life.xlsx" )

for i in $Files
do
  open $i
done
