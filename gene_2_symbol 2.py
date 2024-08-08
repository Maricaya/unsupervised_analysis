
import os
import yaml
import subprocess

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

def run_gene_2_symbol(prefix):
    output_file = f"{prefix}.symbol.tsv"
    log_file = f"logs/gene2symbol/{prefix}.log"
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    species = config["ref"]["species"]
    threads = 1  # Adjust this based on your requirements

    cmd = [
        "Rscript", "scripts/gene2symbol.R",
        f"{prefix}.tsv",
        species,
        output_file
    ]

    with open(log_file, 'w') as log:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    print(f"Finished processing gene_2_symbol for prefix {prefix}")

# Example usage
prefixes = [
    "results/diffexp/treated-vs-untreated.diffexp",
    "results/deseq2/normcounts",
    "results/counts/all"
]

for prefix in prefixes:
    run_gene_2_symbol(prefix)
