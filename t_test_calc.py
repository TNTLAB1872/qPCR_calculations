import pandas as pd
from scipy.stats import ttest_ind

# File path to the Excel file
excel_file_path = '/Users/rahulramakrishnan/Documents/TNT_Lab/qpcr/updated_pval.xlsx'
# Sheet name containing the data
sheet_name = 't_test'

# Read the Excel file
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Define the column names according to the actual data layout
blast_column = 'Test (Blast)'  # Column where Blast ΔCt values are located
sham_column = 'Calibrator (Sham)'   # Column where Sham ΔCt values are located
p_value_column = 'p_val'  # Column where p-values should be stored

# Assume headers are on the first row (index 0), and ΔCt values start on the second row (index 1)
# Iterate over the DataFrame in steps of 4 rows for each gene
for i in range(1, df.shape[0], 4):  # Change 4 to the actual number of rows per gene group if different
    # Get ΔCt values for Blast and Sham, convert to numeric, ignoring non-numeric values
    blast_values = pd.to_numeric(df.loc[i:i+1, blast_column], errors='coerce').dropna()
    sham_values = pd.to_numeric(df.loc[i+2:i+3, sham_column], errors='coerce').dropna()

    # Perform the t-test only if both groups have at least two numeric values
    if len(blast_values) >= 2 and len(sham_values) >= 2:
        t_stat, p_value = ttest_ind(blast_values, sham_values, equal_var=False)
        # Store the p-value in the DataFrame for the first row of the Blast group
        df.loc[i, p_value_column] = p_value
    else:
        # Indicate that there wasn't enough data for a t-test
        df.loc[i, p_value_column] = "Not enough data"

    # Clear the p-values for the rest of the gene group
    df.loc[i+1:i+3, p_value_column] = pd.NA

# Save the DataFrame back to the same Excel file
df.to_excel(excel_file_path, index=False)
