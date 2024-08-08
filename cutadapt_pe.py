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

def get_cutadapt_input(sample, unit):
    fq1 = units.loc[(sample, unit), "fq1"]
    fq2 = units.loc[(sample, unit), "fq2"]
    assert pd.notna(fq1) and pd.notna(fq2), f"Paired-end files not found for sample {sample}, unit {unit}"
    return fq1, fq2

def run_cutadapt_pe(sample, unit):
    fq1, fq2 = get_cutadapt_input(sample, unit)
    output_fq1 = f"results/trimmed/{sample}_{unit}_R1.fastq.gz"
    output_fq2 = f"results/trimmed/{sample}_{unit}_R2.fastq.gz"
    qc_file = f"results/trimmed/{sample}_{unit}.paired.qc.txt"
    log_file = f"logs/cutadapt/{sample}_{unit}.log"
    
    os.makedirs(os.path.dirname(output_fq1), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    adapters = units.loc[(sample, unit), "adapters"]
    extra_params = config.get("params", {}).get("cutadapt-pe", "")

    cutadapt_cmd = [
        "cutadapt",
        "-a", adapters,
        "-A", adapters,
        "-o", output_fq1,
        "-p", output_fq2,
        fq1, fq2,
        extra_params,
    ]

    with open(log_file, 'w') as log:
        process = subprocess.run(cutadapt_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    with open(qc_file, 'w') as qc:
        qc.write(process.stdout.decode())

    print(f"Finished processing {sample} {unit}")

# Example usage
for sample in units.index.get_level_values("sample_name").unique():
    for unit in units.loc[sample].index.get_level_values("unit_name").unique():
        run_cutadapt_pe(sample, unit)
