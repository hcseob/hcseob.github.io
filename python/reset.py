import os
import json
import shutil

# Delete all files in the 'pages' directory
pages_dir = 'pages'
file_name = 'creation_priority.json'
if os.path.exists(pages_dir):
    shutil.rmtree(pages_dir)
    print(f"Deleted all files in directory '{pages_dir}'")
else:
    print(f"Directory '{pages_dir}' does not exist.")

# Create 'pages' directory again (optional)
os.makedirs(pages_dir)
print(f"Recreated directory '{pages_dir}'")

# Initialize a dictionary with a single key-value pair
init_dict = {'Philosophy': 1}

# Create and save the initialized dictionary to 'dictionary_file.json'
with open(f"{pages_dir}/{file_name}", 'w') as f:
    json.dump(init_dict, f)
    print(f"Initialized {file_name} with {init_dict}")