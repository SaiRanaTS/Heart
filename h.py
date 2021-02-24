from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
def fn(x,y,z):
    return ((x**2) + 9*(y**2)/4 + (z**2) - 1)**3-(x**2)*(z**3)-9*(y**2)*(z**3)/80
bbox=(-1.2,1.2)
xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
A = np.linspace(xmin, xmax, 100)
B = np.linspace(xmin, xmax, 50)
A1,A2 = np.meshgrid(A,A)

for z in B:
    X,Y = A1,A2
    Z = fn(X,Y,z)
    cset = ax.contour(X, Y, Z+z, [z], zdir='z',colors='r')

for y in B:
    X,Z = A1,A2
    Y = fn(X,y,Z)
    cset = ax.contour(X, Y+y, Z, [y], zdir='y',colors='r')

for x in B:
    Y,Z = A1,A2
    X = fn(x,Y,Z)
    cset = ax.contour(X+x, Y, Z, [x], zdir='x',colors='r')

ax.set_zlim3d(zmin,zmax)
ax.set_xlim3d(xmin,xmax)
ax.set_ylim3d(ymin,ymax)
plt.title('For Merit', fontdict={'fontsize':15,'fontweight':'bold'})
plt.show()