import os
import subprocess
from datetime import datetime

# Define paths
input_directory = "data/posebusters_inputs"
log_file = "run_infer_log.txt"

# Get the list of input files
input_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

# Initialize counters and log
total_files = len(input_files)
success_count = 0
failure_count = 0

with open(log_file, "w") as log:
    log.write(f"Run started at {datetime.now()}\n")
    log.write(f"Total files to process: {total_files}\n\n")

# Process each file
for index, file_path in enumerate(input_files, start=1):
    print(f"[{index}/{total_files}] Processing: {file_path}")
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

# Final summary
with open(log_file, "a") as log:
    log.write("Run completed.\n")
    log.write(f"Total files: {total_files}\n")
    log.write(f"Successfully processed: {success_count}\n")
    log.write(f"Failures: {failure_count}\n")

print("Processing complete. Check run_infer_log.txt for details.")