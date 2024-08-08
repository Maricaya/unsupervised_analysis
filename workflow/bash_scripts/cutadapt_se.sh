#!/bin/bash
# Bash script for rule cutadapt_se

# Input files
input_files=(get_cutadapt_input,)

# Output files
output_files=(fastq="results/trimmed/{sample}_{unit}_single.fastq.gz",)

# Log file
log_file="logs/cutadapt/{sample}_{unit}.log",

