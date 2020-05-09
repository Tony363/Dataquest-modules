### Make sure to install packages of 'numpy-stl', 'scipy', 'matplotlib' first
### you may use command 'pip' to install such as 'pip install numpy-stl' 
###
### In case there are issues for Windows installation, you can also use
### precompiled packages from "http://www.lfd.uci.edu/~gohlke/pythonlibs/"
### Just download the needed whl packages to your local disk and, e.g. type
### 'pip install C:\Python\packages\scipy-0.16.1-cp27-none-win32.whl'.
from stl import mesh
from stl.mesh import Mesh
from matplotlib import pyplot
from mpl_toolkits import mplot3d
import numpy as np
import math


# Load a STL model from a file
#  - Change 'C:\\Users\\...' to your file's directory. Note that '\\' is used in
#    Windows system. In Linux, use '/' instead.
#my_mesh=mesh.Mesh.from_file('C:\\Users\\Wang\\Yan\\STL\\vases\\tessa_vase_filled.stl')
my_mesh=mesh.Mesh.from_file('tessa_vase_filled.stl')

my_mesh.rotate

def first_method(array,index):
    array[:,:,index] = array[:,:,index] + 60
    return array

def second_method(array,index):
    return mesh.rotate(my_mesh.vectors, math.radians(90))


# Create a new plot 
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)


my_mesh.vectors[:,:,1] =  my_mesh.vectors[:,:,1] + np.pi/4

# my_mesh.vectors[:,:,0] =  my_mesh.vectors[:,:,0] + 60
my_mesh.vectors[:,:,2] = my_mesh.vectors[:,:,2] - np.pi/3

# Add the vectors from the STL mesh model to the plot
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(my_mesh.vectors))

print(my_mesh.vectors)

# Auto scale to the mesh size
scale = my_mesh.points.flatten('F')
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
