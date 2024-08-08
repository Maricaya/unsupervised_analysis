#!/bin/bash
# Bash script for rule pca

# Input files
input_files=("results/deseq2/all.rds",)

# Output files
output_files=(report("results/pca.{variable}.svg", "../report/pca.rst"),)

# Log file
log_file="logs/pca.{variable}.log",

