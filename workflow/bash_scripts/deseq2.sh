#!/bin/bash
# Bash script for rule deseq2

# Input files
input_files=("results/deseq2/all.rds",)

# Output files
output_files=(table=report("results/diffexp/{contrast}.diffexp.tsv", "../report/diffexp.rst"),)

# Log file
log_file="logs/deseq2/{contrast}.diffexp.log",

