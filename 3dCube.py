import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
def cubes(sides):
    data = np.ones(sides)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111 , projection = '3d')
    ax.voxels(data, facecolors="blue")
    plt.show()
def main():
    sides = np.array([ 3, 3, 3 ])
    cubes(sides)
if __name__ == "__main__":
    main ()