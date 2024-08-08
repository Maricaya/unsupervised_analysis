#!/bin/bash
# Bash script for rule rseqc_readdup

# Input files
input_files=("results/star/{sample}_{unit}/Aligned.sortedByCoord.out.bam",)

# Output files
output_files=("results/qc/rseqc/{sample}_{unit}.readdup.DupRate_plot.pdf",)

# Log file
log_file="logs/rseqc/rseqc_readdup/{sample}_{unit}.log",

# Command to execute
read_duplication.py -i {input} -o {params.prefix} > {log} 2>&1
