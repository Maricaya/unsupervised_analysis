import os
import pandas as pd
import yaml
import subprocess

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

# Load units
units = pd.read_csv(config["units"], sep="\t", dtype={"sample_name": str, "unit_name": str})
units.set_index(["sample_name", "unit_name"], drop=False, inplace=True)
units.sort_index(inplace=True)

def run_rseqc_readdis(sample, unit):
    input_bam = f"results/star/{sample}_{unit}/Aligned.sortedByCoord.out.bam"
    output_file = f"results/qc/rseqc/{sample}_{unit}.readdistribution.txt"
    log_file = f"logs/rseqc/rseqc_readdis/{sample}_{unit}.log"
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    annotation_bed = "results/qc/rseqc/annotation.bed"
    rseqc_cmd = [
        "read_distribution.py",
        "-r", annotation_bed,
        "-i", input_bam
    ]

    with open(log_file, 'w') as log:
        process = subprocess.run(rseqc_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())
    
    with open(output_file, 'w') as output:
        output.write(process.stdout.decode())

    print(f"Finished processing rseqc_readdis for {sample} {unit}")

# Example usage
for sample in units.index.get_level_values("sample_name").unique():
    for unit in units.loc[sample].index.get_level_values("unit_name").unique():
        run_rseqc_readdis(sample, unit)

