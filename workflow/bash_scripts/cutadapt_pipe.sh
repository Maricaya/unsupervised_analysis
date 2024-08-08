#!/bin/bash
# Bash script for rule cutadapt_pipe

# Input files
input_files=(get_cutadapt_pipe_input,)

# Output files
output_files=(pipe("pipe/cutadapt/{sample}/{unit}.{fq}.{ext}"),)

# Log file
log_file="logs/pipe-fastqs/catadapt/{sample}_{unit}.{fq}.{ext}.log",

# Command to execute
cat {input} > {output} 2> {log}
