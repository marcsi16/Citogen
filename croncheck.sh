#!/usr/bin/env bash

if [ -e /data/NGS_eval/SENTIEON_OUTPUT/TP53/INPUTCHECK_LOCK.txt ] 
then
	exit 1
else
	/home/marcsi/inputcheck1.sh
fi
