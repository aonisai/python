#!/bin/sh

file $1 | grep -o directory > /dev/null 2>&1
if [ $? -eq 0 ]; then
	ls $1
else
	less $1
	#cat $1
fi
