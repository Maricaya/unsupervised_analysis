#!/bin/bash
# Bash script for rule rseqc_readdis

# Input files
input_files=(bam="results/star/{sample}_{unit}/Aligned.sortedByCoord.out.bam",)

# Output files
output_files=("results/qc/rseqc/{sample}_{unit}.readdistribution.txt",)

# Log file
log_file="logs/rseqc/rseqc_readdis/{sample}_{unit}.log",

# Command to execute
read_distribution.py -r {input.bed} -i {input.bam} > {output} 2> {log}
