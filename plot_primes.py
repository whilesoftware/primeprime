import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
df = pd.read_csv('data/primes.txt', header=None, names=['n', 'prime', 'diff'])
n = df['n']
p = df['prime']
diff = df['diff']

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(n, diff)

ax.set(xlabel='n', ylabel='difference from previous prime',
       title='prime numbers')
ax.grid()

fig.savefig("test.png")
plt.show()
