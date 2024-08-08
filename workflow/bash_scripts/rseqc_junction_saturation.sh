#!/bin/bash
# Bash script for rule rseqc_junction_saturation

# Input files
input_files=(bam="results/star/{sample}_{unit}/Aligned.sortedByCoord.out.bam",)

# Output files
output_files=("results/qc/rseqc/{sample}_{unit}.junctionsat.junctionSaturation_plot.pdf",)

# Log file
log_file="logs/rseqc/rseqc_junction_saturation/{sample}_{unit}.log",

# Command to execute
junction_saturation.py {params.extra} -i {input.bam} -r {input.bed} -o {params.prefix}
