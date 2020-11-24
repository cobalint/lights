import numpy as np
import seaborn as sns
import matplotlib
import math

l_x = 1000
l_y = 1000

on = np.zeros([l_x, l_y])
l = np.zeros([l_x, l_y])
t = np.zeros([l_x, l_y])

on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1
on[np.random.randint(l_x), np.random.randint(l_y)] = 1


where = np.transpose(np.array(np.where(on == 1)))
temp = np.zeros(len(where))
d = np.zeros([l_x, l_y])


for i in range(l_x):
    for j in range(l_y):
        for k in range(len(where)):
            temp[k] = math.log(1/ (((((where[k, 1] - i) ** 2) + ((where[k, 0] - j) ** 2)) ** (1/2)) + 1))
        d[i, j] = np.mean(temp, axis = 0)
        temp = np.zeros(len(where))


sns.heatmap(d, cmap = "mako")
matplotlib.pyplot.show()

math.log(1 / (np.min(temp, axis = 0) + 1), 7)