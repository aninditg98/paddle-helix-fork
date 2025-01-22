import os
import subprocess
from datetime import datetime
from tqdm import tqdm

# Define paths
input_directory = "data/posebusters_inputs"
output_directory = "output"
log_file = "run_infer_log2.txt"

# Get the list of input files
input_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

print(f"Total files: {len(input_files)}")

# Filter out files with existing output directories
input_files = [f for f in input_files if not os.path.exists(os.path.join(output_directory, os.path.splitext(os.path.basename(f))[0]))]

print(f"Files to work on: {len(input_files)}")

# Initialize counters and log
total_files = len(input_files)
success_count = 0
failure_count = 0

with open(log_file, "w") as log:
    log.write(f"Run started at {datetime.now()}\n")
    log.write(f"Total files to process: {total_files}\n\n")

# Process each file
progress_bar = tqdm(input_files, desc=f"Processing files | Success: {success_count}, Failure: {failure_count}", unit="file")
for index, file_path in enumerate(progress_bar, start=1):
    output_dir = os.path.join(output_directory, os.path.splitext(os.path.basename(file_path))[0])

    tqdm.write(f"[{index}/{total_files}] Processing: {file_path}")
    try:
        # Run the command
        result = subprocess.run(["./run_infer.sh", file_path], capture_output=True, text=True)

        # Log the output
        with open(log_file, "a") as log:
            log.write(f"[{index}/{total_files}] {file_path}\n")
            log.write(f"Exit Code: {result.returncode}\n")
            log.write(f"Output:\n{result.stdout}\n")
            if result.returncode != 0:
                log.write(f"Error:\n{result.stderr}\n")
                failure_count += 1
            else:
                success_count += 1
            log.write("\n")
    except Exception as e:
        # Log unexpected exceptions
        with open(log_file, "a") as log:
            log.write(f"[{index}/{total_files}] {file_path} FAILED with Exception:\n{e}\n\n")
        failure_count += 1

    # Update the progress bar description
    progress_bar.set_description(f"Processing files | Success: {success_count}, Failure: {failure_count}")

# Final summary
with open(log_file, "a") as log:
    log.write("Run completed.\n")
    log.write(f"Total files: {total_files}\n")
    log.write(f"Successfully processed: {success_count}\n")
    log.write(f"Failures: {failure_count}\n")

print(f"Processing complete. Check {log_file} for details.")
