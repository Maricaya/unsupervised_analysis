
import os
import yaml
import subprocess

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

def run_get_genome():
    output_file = "resources/genome.fasta.gz"  # 修改文件名，添加.gz后缀
    log_file = "logs/get-genome.log"
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    species = config["ref"]["species"]
    build = config["ref"]["build"]
    release = config["ref"]["release"]

    # 下载基因组序列的示例命令
    cmd = [
        "wget",
        f"ftp://ftp.ensembl.org/pub/release-{release}/fasta/{species}/dna/{species}.{build}.dna.toplevel.fa.gz",  # 修改下载路径
        "-O", output_file
    ]

    with open(log_file, 'w') as log:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.write(process.stdout.decode())
        log.write(process.stderr.decode())

    print(f"Finished processing get_genome")

# Example usage
run_get_genome()
