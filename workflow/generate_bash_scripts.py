import re
import os

# Define the Snakefile path and output directory for bash scripts
snakefile_path = 'Snakefile'
output_dir = 'bash_scripts'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the Snakefile
with open(snakefile_path, 'r') as file:
    content = file.read()

# Regex pattern to find all rules
rule_pattern = re.compile(r'rule (\w+):\n(.*?)(?=\nrule|\Z)', re.DOTALL)

# Iterate over all rules
for match in rule_pattern.finditer(content):
    rule_name = match.group(1)
    rule_body = match.group(2)

    # Extract key components from the rule
    input_files = re.findall(r'input:\s*(.*)', rule_body)
    output_files = re.findall(r'output:\s*(.*)', rule_body)
    log_file = re.findall(r'log:\s*(.*)', rule_body)
    command = re.findall(r'shell:\s*"(.*?)"', rule_body, re.DOTALL)

    # Create a corresponding bash script
    bash_script = f"#!/bin/bash\n# Bash script for rule {rule_name}\n\n"
    
    # Add input files
    if input_files:
        bash_script += f"# Input files\ninput_files=({input_files[0].strip()})\n\n"

    # Add output files
    if output_files:
        bash_script += f"# Output files\noutput_files=({output_files[0].strip()})\n\n"

    # Add log file
    if log_file:
        bash_script += f"# Log file\nlog_file={log_file[0].strip()}\n\n"

    # Add the command
    if command:
        bash_script += f"# Command to execute\n{command[0].strip()}\n"

    # Save the bash script to the output directory
    bash_script_path = os.path.join(output_dir, f"{rule_name}.sh")
    with open(bash_script_path, 'w') as bash_file:
        bash_file.write(bash_script)

    # Make the script executable
    os.chmod(bash_script_path, 0o755)

print("Bash scripts generated successfully.")
