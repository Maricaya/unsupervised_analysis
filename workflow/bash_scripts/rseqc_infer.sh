#!/bin/bash
# Bash script for rule rseqc_infer

# Input files
input_files=(bam="results/star/{sample}_{unit}/Aligned.sortedByCoord.out.bam",)

# Output files
output_files=("results/qc/rseqc/{sample}_{unit}.infer_experiment.txt",)

# Log file
log_file="logs/rseqc/rseqc_infer/{sample}_{unit}.log",

# Command to execute
infer_experiment.py -r {input.bed} -i {input.bam} > {output} 2> {log}
