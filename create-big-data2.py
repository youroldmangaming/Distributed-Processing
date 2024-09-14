import pandas as pd
import numpy as np

# Parameters
num_rows = 4000000
chunk_size = 1000
sig_figs = 6  # Desired number of significant figures

# Function to format values with significant figures
def set_significant_figures(value, sig_figs):
    if value == 0:
        return 0
    else:
        # Use string formatting to enforce the number of significant figures
        return float(f"{value:.{sig_figs}g}")  # Format to significant figures

# Define column names and data
ids = np.arange(1, num_rows + 1)
names = ['Name_' + str(i) for i in range(num_rows)]
values = np.random.random(size=num_rows)

# Apply significant figures to the 'values' array
values = np.array([set_significant_figures(val, sig_figs) for val in values])

# Generate and write CSV in chunks
for start in range(0, num_rows, chunk_size):
    end = min(start + chunk_size, num_rows)
    df = pd.DataFrame({
        'ID': ids[start:end],
        'Name': names[start:end],
        'Value': values[start:end]
    })
    df.to_csv('large_file.csv', mode='a', header=(start == 0), index=False)

print("CSV file with values formatted to consistent significant figures has been created.")
