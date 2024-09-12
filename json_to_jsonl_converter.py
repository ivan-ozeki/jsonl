import os
import json

# Step 1: Define the directories for input JSON files and output JSONL files
input_directory = '/Users/ivanassenov/dev/R&D/crawler/Data/page3'  # Directory containing the JSON files
output_directory = '/Users/ivanassenov/dev/R&D/jsonl/output-jsonl-data'  # Directory where JSONL files will be saved

# Step 2: Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Step 3: Function to convert JSON to JSONL
def convert_json_to_jsonl(input_file, output_file):
    """
    Converts a JSON file with 'clauses' structure to JSONL format and saves it.
    
    Parameters:
    - input_file: str, path to the input JSON file
    - output_file: str, path to the output JSONL file
    """
    with open(input_file, 'r') as f:
        data = json.load(f)  # Load JSON data from file
    
    # Extract clauses from the JSON data
    clauses = data.get('clauses', [])  # Get the 'clauses' array
    
    with open(output_file, 'w') as f_out:
        # Iterate over each clause and write it to JSONL format
        for clause in clauses:
            json.dump(clause, f_out)
            f_out.write('\n')  # Newline after each JSON object

# Step 4: Process each file in the input directory
def process_files_in_directory(input_directory, output_directory):
    """
    Processes all JSON files in the input directory, converts them to JSONL, 
    and saves them in the output directory.
    
    Parameters:
    - input_directory: str, path to the directory containing the JSON files
    - output_directory: str, path to the directory to save JSONL files
    """
    processed_files = []  # List to store the processed file paths
    
    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.json'):  # Process only JSON files
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename.replace('.json', '.jsonl'))
            
            # Convert JSON to JSONL
            convert_json_to_jsonl(input_file_path, output_file_path)
            
            # Record the processed file
            processed_files.append(input_file_path)
            print(f"Processed: {input_file_path} -> {output_file_path}")
    
    return processed_files

# Step 5: Run the program to process the files
processed_files = process_files_in_directory(input_directory, output_directory)

# Print a summary of the processed files
print(f"Total files processed: {len(processed_files)}")
for file in processed_files:
    print(f"Processed file: {file}")
