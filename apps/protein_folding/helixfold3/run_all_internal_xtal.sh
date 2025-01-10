#!/bin/bash

DIRECTORY="data/internal_xtal_inputs"

# Check if the provided path is a valid directory
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: $DIRECTORY is not a valid directory."
    exit 1
fi

echo "Files in $DIRECTORY:"
for FILE in "$DIRECTORY"/*; do
    if [ -f "$FILE" ]; then
        ./run_infer.sh "$FILE"
    fi
done