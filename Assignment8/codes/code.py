from scipy.stats import binom
import matplotlib.pyplot as plt
# setting the values
# of n and p
n = 5
p = 0.25
# defining list of r values
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph
plt.stem(r_values, dist)
plt.title('Probability Mass Function')
plt.xlabel('$Y$')
plt.ylabel('Probability')
plt.show()
