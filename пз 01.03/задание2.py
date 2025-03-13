import numpy as np
import matplotlib.pyplot as plt


num_GP = 5
GP = np.random.rand(num_GP, 2) * 100
num_SP = 10
plt.figure(figsize=(15, 8))
SP = [i + np.random.normal(0, 5, (num_SP, 2)) for i in GP]
CP = np.array([np.mean(i, axis=0) for i in SP])
POG = [np.std(i, axis=0) for i in SP]

colors = ['blue', 'red', 'green', 'orange', 'purple']

for i in range(len(SP)):
    plt.scatter(SP[i][:, 0], SP[i][:, 1], color=colors[i], alpha=0.6, label='Группа точек ' + str(i + 1))

for i in range(len(CP)):
    plt.errorbar(CP[i][0], CP[i][1], xerr=POG[i][0], yerr=POG[i][1], fmt='o', color='black',
                     capsize=5, label='Центральная точка ' + str(i + 1))

plt.scatter(GP[:, 0], GP[:, 1], color='black', marker='X', s=100, label='Начальные точки')

plt.title('График смещенных точек')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.legend()
plt.axis('equal')

plt.show()