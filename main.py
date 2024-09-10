from binomial_compensation import plot_binomial_prob, max_compensation, average_compensation

# Plot binomial probability for N = 100, p = 0.5
plot_binomial_prob(100, 0.5)

# Calculate maximum compensation for N = 100, p = 0.5, L = 100, m = 10
compensation = max_compensation(100, 0.5, 100, 10)
print(f"The maximum compensation to offer is: {compensation}")

# Calculate average compensation for given L and m
L = 100
m = 5
avg_comp = average_compensation(L, m)
print(f"The average compensation to offer is: {avg_comp}")
