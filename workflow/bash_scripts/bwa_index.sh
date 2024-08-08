#!/bin/bash
# Bash script for rule bwa_index

# Input files
input_files=("resources/genome.fasta",)

# Output files
output_files=(multiext("resources/genome.fasta", ".amb", ".ann", ".bwt", ".pac", ".sa"),)

# Log file
log_file="logs/bwa_index.log",

