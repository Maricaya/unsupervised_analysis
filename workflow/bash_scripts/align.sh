#!/bin/bash
# Bash script for rule align

# Input files
input_files=(unpack(get_fq),)

# Output files
output_files=(aln="results/star/{sample}_{unit}/Aligned.sortedByCoord.out.bam",)

# Log file
log_file="logs/star/{sample}_{unit}.log",

