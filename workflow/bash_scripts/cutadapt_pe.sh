#!/bin/bash
# Bash script for rule cutadapt_pe

# Input files
input_files=(get_cutadapt_input,)

# Output files
output_files=(fastq1="results/trimmed/{sample}_{unit}_R1.fastq.gz",)

# Log file
log_file="logs/cutadapt/{sample}_{unit}.log",

