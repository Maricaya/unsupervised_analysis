
import os
import yaml
import subprocess

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

def run_star_index():
    output_dir = "resources/star_genome"
    log_file = "logs/star_index_genome.log"
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    fasta = "resources/genome.fasta"
    annotation = "resources/genome.gtf"
    threads = 4

    cmd = [
        "STAR",
        "--runThreadN", str(threads),
        "--runMode", "genomeGenerate",
        "--genomeDir", output_dir,
        "--genomeFastaFiles", fasta,
        "--sjdbGTFfile", annotation,
        "--sjdbOverhang", "100"
    ]

    with open(log_file, 'w') as log:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    print(f"Finished processing star_index")

# Example usage
run_star_index()
