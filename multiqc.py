
import os
import yaml
import subprocess
import pandas as pd

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

# Load units
units = pd.read_csv(config["units"], sep="\t", dtype={"sample_name": str, "unit_name": str})
units.set_index(["sample_name", "unit_name"], drop=False, inplace=True)
units.sort_index(inplace=True)

def run_multiqc():
    output_file = "results/qc/multiqc_report.html"
    log_file = "logs/multiqc.log"
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    input_files = []
    for unit in units.itertuples():
        sample_name, unit_name = unit.sample_name, unit.unit_name
        input_files.extend([
            f"results/star/{sample_name}_{unit_name}/Aligned.sortedByCoord.out.bam",
            f"results/qc/rseqc/{sample_name}_{unit_name}.junctionanno.junction.bed",
            f"results/qc/rseqc/{sample_name}_{unit_name}.junctionsat.junctionSaturation_plot.pdf",
            f"results/qc/rseqc/{sample_name}_{unit_name}.infer_experiment.txt",
            f"results/qc/rseqc/{sample_name}_{unit_name}.stats.txt",
            f"results/qc/rseqc/{sample_name}_{unit_name}.inner_distance_freq.inner_distance.txt",
            f"results/qc/rseqc/{sample_name}_{unit_name}.readdistribution.txt",
            f"results/qc/rseqc/{sample_name}_{unit_name}.readdup.DupRate_plot.pdf",
            f"results/qc/rseqc/{sample_name}_{unit_name}.readgc.GC_plot.pdf",
            f"logs/rseqc/rseqc_junction_annotation/{sample_name}_{unit_name}.log"
        ])

    cmd = ["multiqc"] + input_files + ["-o", output_file]

    with open(log_file, 'w') as log:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    print(f"Finished processing multiqc")

# Example usage
run_multiqc()
