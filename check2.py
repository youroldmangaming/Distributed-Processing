import pandas as pd
import numpy as np

def process_large_file(file_path, precision=6):
    try:
        # Read the CSV file and handle the header
        # We skip the header while specifying the dtype because the header is not part of the data
        df = pd.read_csv(file_path, header=0, dtype={'ID': str, 'Name': str, 'Value': str}, low_memory=False)

        # Convert the 'Value' column to float, and coerce errors (invalid values become NaN)
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

        # Drop rows where 'Value' is NaN (invalid values)
        df = df.dropna(subset=['Value'])

        # Convert 'Value' back to float after coercion
        df['Value'] = df['Value'].astype(float)

        # Sum the values and count the valid entries
        total_sum = df['Value'].sum()
        total_count = df['Value'].count()

        print(f"Total Sum from the large file: {total_sum}")
        print(f"Total Count of values: {total_count}")

        # Optionally save the cleaned DataFrame to a new CSV
        df.to_csv('processed_large_file.csv', index=False)

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def main():
    file_path = 'large_file.csv'  # Path to your CSV file
    process_large_file(file_path)

if __name__ == "__main__":
    main()


