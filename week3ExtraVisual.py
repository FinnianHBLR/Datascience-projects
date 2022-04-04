import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib.colors import ListedColormap
import numpy as np

def start():

    N = 50
    x = np.linspace(0, 2*math.pi, N)
    y = [math.sin(i) for i in x]

    vals = np.empty([N, 4])
    vals[:, 0] = np.linspace(0, 131 / 255, N)
    vals[:, 1] = np.linspace(132 / 255, 184 / 255, N)
    vals[:, 2] = np.linspace(77 / 255, 26 / 255, N)
    vals[:, 3] = np.linspace(1, 0.2, N)
    my_map = ListedColormap(vals)

    my_map = ListedColormap(vals)

    plt.figure()
    plt.scatter(x,y, cmap=my_map, c=np.linspace(0,1,N), marker="s", s=np.linspace(10,4000, N))
    plt.show()

if __name__ == '__main__':
    start()
