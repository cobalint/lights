import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import os

if not os.path.exists("images"):
    os.mkdir("images")

np.random.seed(0)

l_x = 300
l_y = 300
points = 60

lum = np.zeros([points, 1])

on = np.zeros([l_x, l_y])



counter = 0
while counter != points:
    on[np.random.randint(l_x), np.random.randint(l_y)] = 1
    lum[counter, 0] = abs(np.random.standard_cauchy())
    #lum[counter, 0] = abs(np.random.normal(0, 10))
    counter += 1


where = np.transpose(np.array(np.where(on != 0)))
temp = np.zeros(points)
d = np.zeros([l_x, l_y])

value = 0

for i in range(l_x):
    for j in range(l_y):
        for k in range(points):
            temp[k] = lum[k, 0] / (math.log((((((where[k, 1] - i) ** 2) + ((where[k, 0] - j) ** 2)) ** (1 / 2)) + 1), 10000) + 0.1)
        d[i, j] = np.mean(temp, axis=0)
        temp = np.zeros(len(where))

# log bases that look good: 1000, 10 000
# 300, 300, 60

plt.style.use('dark_background')
plt.figure()
fig = sns.heatmap(d, cmap="mako", cbar=False, xticklabels=False, yticklabels=False)
name = "images/stars_cauchy.png"
plt.savefig(name, pad_inches=0, bbox_inches='tight')
