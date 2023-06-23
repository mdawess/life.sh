#!/usr/local/bin/zsh

if test "$1" = "pdf" 
then
    'python3.10' pdf.py "$2" "$3" ~/Desktop/
elif test "$1" = "open"
then
  echo "hello, world"
else
    echo "First argument must be one of 'pdf', 'open'"
fi
