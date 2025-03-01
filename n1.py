import matplotlib.pyplot as plt


x = [_ for _ in range(10)]
plt.plot(x, x, color = 'r')
y = [x[i] * 2 for i in range(10)]
plt.plot(x, y, color = 'g')
y = [x[i] * 3 for i in range(10)]
plt.plot(x, y, color = 'b')
y = [x[i] ** 2 for i in range(10)]
plt.plot(x, y, color = 'y')
y = [2 * x[i]**2 for i in range(10)]
plt.plot(x, y, color = 'grey')
plt.show()