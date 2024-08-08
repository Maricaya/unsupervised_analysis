#!/bin/bash
# Bash script for rule rseqc_stat

# Input files
input_files=("results/star/{sample}_{unit}/Aligned.sortedByCoord.out.bam",)

# Output files
output_files=("results/qc/rseqc/{sample}_{unit}.stats.txt",)

# Log file
log_file="logs/rseqc/rseqc_stat/{sample}_{unit}.log",

# Command to execute
bam_stat.py -i {input} > {output} 2> {log}
