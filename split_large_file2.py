import pandas as pd
import numpy as np
import os

# Parameters
input_file = 'large_file.csv'

output_dir = 'split'
num_parts =40
rows_per_part = None  # This will be calculated

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the CSV file to determine the number of rows
total_rows = sum(1 for _ in open(input_file)) - 1  # Subtract 1 for the header
rows_per_part = total_rows // num_parts
print(f"Total rows: {total_rows}, Rows per part: {rows_per_part}")

# Read the large CSV file in chunks and split it
chunk_size = 100000  # Adjust if needed to manage memory

start_row = 0

for part_number in range(num_parts):
    end_row = start_row + rows_per_part

    if end_row > total_rows:
        end_row = total_rows

    # Read a chunk of the file
    chunk = pd.read_csv(input_file, skiprows=range(1, start_row + 1), nrows=rows_per_part)
#   chunk[2] = pd.to_numeric(chunk[2], errors='coerce')
    #chunk = pd.read_csv(input_file, skiprows=range(1, start_row + 1),nrows=rows_per_part, engine='python', low_memory=False, dtype={0: int, 1: str, 2: float})




    # Generate filenames according to the specified pattern
    node_number = (part_number // 10) + 1

    file_suffix = (part_number % 10) + 1

    output_file = os.path.join(output_dir, f'Node{node_number}-{file_suffix}.csv')

    # Write chunk to a new CSV file
    chunk.to_csv(output_file, index=False)

    # Update the start row for the next chunk
    start_row = end_row

print("Splitting complete.")



