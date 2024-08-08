
import os
import yaml
import subprocess

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

def run_deseq2_init():
    output_file1 = "results/deseq2/all.rds"
    output_file2 = "results/deseq2/normcounts.tsv"
    log_file = "logs/deseq2/init.log"
    
    os.makedirs(os.path.dirname(output_file1), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    input_file = "results/counts/all.tsv"
    threads = 1  # Adjust this based on your requirements

    cmd = [
        "Rscript", "scripts/deseq2-init.R",
        input_file,
        output_file1,
        output_file2
    ]

    with open(log_file, 'w') as log:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    print(f"Finished processing deseq2_init")

# Example usage
run_deseq2_init()
