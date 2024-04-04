
import os
# Get the current directory
current_directory = os.path.dirname(__file__)

# Define the path to the folder containing text files (assuming it's named "docs")
folder_path = os.path.join(current_directory, "docs")

# Read content from each text file and store in a list
docs = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            docs.append(content)