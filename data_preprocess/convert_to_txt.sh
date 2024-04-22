#!/bin/bash

# Set the path to the folder containing DOCX files
input_folder="/Users/yinanli/Downloads/382XX"


# Loop through each DOCX file in the folder
for file in "$input_folder"/*.docx; do
    # Extract the filename without extension
    filename=$(basename "$file" .docx)
    # Convert DOCX file to TXT using Pandoc
    pandoc "$file" -o "$input_folder/$filename.txt"
done
