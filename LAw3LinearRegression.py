import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# generate 20 random numbers
x = np.random.uniform(-7, 7, (20,1))
# y = x*3 + 7 + random noise
y = np.array([elem*3 + 7 + np.random.uniform(-5,5) for elem in x])

reg = LinearRegression().fit(x, y)
y_hat = reg.predict(x)

plt.scatter(x,y, label='Data with noise')
plt.plot(x, y_hat, c='r', label='Linear regressor')
plt.legend()
plt.savefig('linreg.png')  # if you want to save the plot
plt.show()