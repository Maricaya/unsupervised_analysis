import os
import glob
import pandas as pd
import yaml

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

# Load samples
samples = pd.read_csv(config["samples"], sep="\t", dtype={"sample_name": str})

# Load units
units = pd.read_csv(config["units"], sep="\t", dtype={"sample_name": str, "unit_name": str})
units.set_index(["sample_name", "unit_name"], drop=False, inplace=True)
units.sort_index(inplace=True)

def get_cutadapt_pipe_input(sample, unit, fq):
    file_path = units.loc[(sample, unit), fq]
    assert file_path, f"No file found for sample {sample}, unit {unit}, fq {fq}"
    return [file_path]

def run_cutadapt_pipe(sample, unit):
    for fq in ["fq1", "fq2"]:
        if pd.notna(units.loc[(sample, unit), fq]):
            input_files = get_cutadapt_pipe_input(sample, unit, fq)
            ext = os.path.splitext(input_files[0])[1].lstrip('.')
            output_file = f"pipe/cutadapt/{sample}/{unit}.{fq}.{ext}"
            log_file = f"logs/pipe-fastqs/catadapt/{sample}_{unit}.{fq}.{ext}.log"
            
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

            with open(log_file, 'w') as log:
                with open(output_file, 'w') as output:
                    for input_file in input_files:
                        with open(input_file, 'r') as infile:
                            output.write(infile.read())
                            log.write(f"Processed {input_file}\n")
            print(f"Finished processing {sample} {unit} {fq} {ext}")

# Example usage
for sample in samples["sample_name"]:
    try:
        for unit in units.loc[sample].index.get_level_values("unit_name").unique():
            run_cutadapt_pipe(sample, unit)
    except KeyError:
        print(f"No units found for sample {sample}")
