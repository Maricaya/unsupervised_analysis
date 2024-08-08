#!/bin/bash
# Bash script for rule rseqc_innerdis

# Input files
input_files=(bam="results/star/{sample}_{unit}/Aligned.sortedByCoord.out.bam",)

# Output files
output_files=("results/qc/rseqc/{sample}_{unit}.inner_distance_freq.inner_distance.txt",)

# Log file
log_file="logs/rseqc/rseqc_innerdis/{sample}_{unit}.log",

# Command to execute
inner_distance.py -r {input.bed} -i {input.bam} -o {params.prefix} > {log} 2>&1
