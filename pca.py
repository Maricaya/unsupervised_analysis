
import os
import yaml
import subprocess

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

def run_pca(variable):
    output_file = f"results/pca.{variable}.svg"
    log_file = f"logs/pca.{variable}.log"
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    input_file = "results/deseq2/all.rds"
    threads = 1  # Adjust this based on your requirements

    cmd = [
        "Rscript", "scripts/plot-pca.R",
        input_file,
        variable,
        output_file
    ]

    with open(log_file, 'w') as log:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    print(f"Finished processing pca for variable {variable}")

# Example usage
for variable in config["diffexp"]["variables_of_interest"]:
    run_pca(variable)
