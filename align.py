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

def get_fq(sample, unit):
    fq1 = units.loc[(sample, unit), "fq1"]
    fq2 = units.loc[(sample, unit), "fq2"]
    return fq1, fq2

def run_star_align(sample, unit):
    fq1, fq2 = get_fq(sample, unit)
    output_dir = f"results/star/{sample}_{unit}/"
    output_prefix = os.path.join(output_dir, "Aligned.")
    os.makedirs(output_dir, exist_ok=True)
    
    log_file = f"logs/star/{sample}_{unit}.log"
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    star_index = "resources/star_genome"
    annotation_file = "resources/genome.gtf"

    star_cmd = [
        "STAR",
        "--runThreadN", str(24),
        "--genomeDir", star_index,
        "--sjdbGTFfile", annotation_file,
        "--readFilesIn", fq1, fq2,
        "--readFilesCommand", "zcat",
        "--outFileNamePrefix", output_prefix,
        "--outSAMtype", "BAM", "SortedByCoordinate",
        "--quantMode", "GeneCounts"
    ]

    extra_params = config.get("params", {}).get("star", "")
    if extra_params:
        star_cmd.extend(extra_params.split())

    with open(log_file, 'w') as log:
        process = subprocess.run(star_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    print(f"Finished processing {sample} {unit}")

# Example usage
for sample in units.index.get_level_values("sample_name").unique():
    for unit in units.loc[sample].index.get_level_values("unit_name").unique():
        run_star_align(sample, unit)
