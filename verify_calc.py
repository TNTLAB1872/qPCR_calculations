from scipy.stats import ttest_ind

# ΔCt values for the first gene's Blast and Sham groups
blast_values = [5.94, 6.748]  # Test (Blast) ΔCt values for the first gene
sham_values = [6.903, 6.374]  # Calibrator (Sham) ΔCt values for the first gene

# Perform the t-test
t_stat, p_value = ttest_ind(6.344, 6.638, equal_var=False)

print(p_value)
