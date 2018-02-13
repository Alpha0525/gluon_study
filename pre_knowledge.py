from mxnet import ndarray as nd
import numpy as np
x = nd.arange(0,9).reshape((3,3))
print('x: ', x)
print(x[1:3,0:3])

# y=y+x
# after=id(y)
# print(after)

# print ("x:{}\n y:{}\n z:{}\n".format(x,y,z))