
import os
import yaml
import subprocess

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

def run_deseq2(contrast):
    output_table = f"results/diffexp/{contrast}.diffexp.tsv"
    output_ma_plot = f"results/diffexp/{contrast}.ma-plot.svg"
    log_file = f"logs/deseq2/{contrast}.diffexp.log"
    
    os.makedirs(os.path.dirname(output_table), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    input_file = "results/deseq2/all.rds"
    threads = 1  # Adjust this based on your requirements

    cmd = [
        "Rscript", "scripts/deseq2.R",
        input_file,
        contrast,
        output_table,
        output_ma_plot
    ]

    with open(log_file, 'w') as log:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    print(f"Finished processing deseq2 for contrast {contrast}")

# Example usage
for contrast in config["diffexp"]["contrasts"]:
    run_deseq2(contrast)
