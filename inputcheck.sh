#!/usr/bin/env bash
INPUTCHECK_LOCK="INPUTCHECK_LOCK.txt"
echo $(date +"%m_%d_%Y_%H_%M") " Inputcheck1.sh is currently running. This file will be automatically deleted." > /data/NGS_eval/SENTIEON_OUTPUT/TP53/$INPUTCHECK_LOCK
ls -A /data/NGS_eval/SENTIEON_INPUT/TP53
if [ "$(ls -A /data/NGS_eval/SENTIEON_INPUT/TP53)" ]; then
	DBFASTQ=$(ls -lR /data/NGS_eval/SENTIEON_INPUT/TP53/*.fastq.gz |wc -l)
		#Check if the number of files are even or odd.
		if [ 'expr $DBFASTQ % 2 == 0' ]; then
			yes "\r" | /data/NGS_eval/Sentieon/call_batch.sh tp53_amplicon.sh /data/NGS_eval/SENTIEON_INPUT/TP53 /data/NGS_eval/SENTIEON_OUTPUT/TP53
			DBVCF=$(find /data/NGS_eval/SENTIEON_OUTPUT/TP53 -mindepth 1 -maxdepth 1 -type d |wc -l)
			EXPECTEDDBVCF=$((DBFASTQ/2+DBVCF))
				while [ $DBVCF -ne $EXPECTEDDBVCF ]
				do
					sleep 1m
					DBVCF=$(find /data/NGS_evalSENTIEON_OUTPUT/TP53 -mindepth 1 -maxdepth 1 -type d |wc -l);
				done
			NOW=$(date +"%m_%d_%Y_%H_%M")
			FILE="log_$NOW.txt"
			ls -A /data/NGS_eval/SENTIEON_INPUT/TP53 >> /data/NGS_eval/SENTIEON_OUTPUT/TP53/$FILE
			ls -A /data/NGS_eval/SENTIEON_OUTPUT/TP53 >> /data/NGS_eval/SENTIEON_OUTPUT/TP53/$FILE
			echo $DBFASTQ" db fastq file feldolgozása" $((DBFASTQ/2)) " db vcf filet eredményezett." >> /data/NGS_eval/SENTIEON_OUTPUT/TP53/$FILE
			sleep 2m
			rm -f /data/NGS_eval/SENTIEON_INPUT/TP53/*
		#	mv /data/NGS_eval/SENTIEON_OUTPUT/TP53/*/*.vcf.gz /data/NGS_eval/SENTIEON_OUTPUT/TP53
		#	mv /data/NGS_eval/SENTIEON_OUTPUT/TP53/*/*.bam /data/NGS_eval/SENTIEON_OUTPUT/TP53
		#	rm -f /data/NGS_eval/SENTIEON_OUTPUT/TP53/INPUTCHECK_LOCK.txt
		else
			NOW=$(date +"%m_%d_%Y")
			FILE="log_$NOW.txt"
		#	ls -A /data/NGS_eval/SENTIEON_INPUT/TP53 >> /data/NGS_eval/SENTIEON_OUTPUT/TP53/$FILE
			echo $(date +"%H_%M")" Páratlan számú fileok az input mappában." > /data/NGS_eval/SENTIEON_OUTPUT/TP53/$FILE 
			rm -f /data/NGS_eval/SENTIEON_OUTPUT/TP53/INPUTCHECK_LOCK.txt
		fi
else
	NOW=$(date +"%m_%d_%Y")
	FILE="log_$NOW.txt"
	echo $(date +"%H_%M")" Egy vagy több file hiányzik a mappából." > /data/NGS_eval/SENTIEON_OUTPUT/TP53/$FILE;
	rm -f /data/NGS_eval/SENTIEON_OUTPUT/TP53/INPUTCHECK_LOCK.txt
fi
