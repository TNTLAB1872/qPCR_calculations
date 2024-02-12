import numpy as np

# Ct values for individual samples
blast_ct_values = [5.940, 6.790]  # Test (Blast) samples
sham_ct_values = [6.903, 6.374]   # Calibrator (Sham) samples

# Calculate average ΔCt for Test (Blast) and Calibrator (Sham)
average_blast_ct = np.mean(blast_ct_values)
average_sham_ct = np.mean(sham_ct_values)

# Calculate ΔΔCt
delta_delta_ct = average_blast_ct - average_sham_ct

# Calculate 2^-ΔCt for each sample
blast_2_delta_ct = [2**(-ct) for ct in blast_ct_values]
sham_2_delta_ct = [2**(-ct) for ct in sham_ct_values]

# Calculate 2^-ΔΔCt
fold_change_2_delta_delta_ct = 2**(-delta_delta_ct)

# Print results in a readable format
print("2^-ΔCt Values:")
print("==============")
print(f"Blast Samples: {', '.join(f'{value:.3f}' for value in blast_2_delta_ct)}")
print(f"Sham Samples: {', '.join(f'{value:.3f}' for value in sham_2_delta_ct)}")
print("\nFold Change (2^-ΔΔCt):")
print("======================")
print(f"{fold_change_2_delta_delta_ct:.3f}")
