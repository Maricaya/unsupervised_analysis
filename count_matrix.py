
import os
import pandas as pd
import yaml

# Load configuration
with open("config/config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

# Load units
units = pd.read_csv(config["units"], sep="\t", dtype={"sample_name": str, "unit_name": str})
units.set_index(["sample_name", "unit_name"], drop=False, inplace=True)
units.sort_index(inplace=True)

def run_count_matrix():
    output_file = "results/counts/all.tsv"
    log_file = "logs/count-matrix.log"
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    input_files = [f"results/star/{unit.sample_name}_{unit.unit_name}/ReadsPerGene.out.tab" for unit in units.itertuples()]
    samples = units["sample_name"].tolist()
    strand = ["yes" if x == "yes" else "no" for x in units["strandedness"].tolist()]

    counts_dict = {}
    for sample, input_file in zip(samples, input_files):
        with open(input_file) as f:
            for line in f:
                gene, unstranded, stranded_f, stranded_r = line.strip().split()
                if gene not in counts_dict:
                    counts_dict[gene] = []
                counts_dict[gene].append(int(unstranded if strand[samples.index(sample)] == "no" else stranded_f))

    counts_df = pd.DataFrame.from_dict(counts_dict, orient="index", columns=samples)
    counts_df.to_csv(output_file, sep="\t")

    with open(log_file, 'w') as log:
        log.write("Count matrix generated successfully.")

    print(f"Finished processing count matrix")

# Example usage
run_count_matrix()
