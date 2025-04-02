import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


def plot(x, y):
    plt.plot(x,y)
    plt.axvline(0, color='r')
    plt.axhline(0, color='g')
    plt.show()

if __name__ == "__main__":
    x = np.arange(-5, 5, 0.1)
    y = np.sin(x)
    plot(x, y)

