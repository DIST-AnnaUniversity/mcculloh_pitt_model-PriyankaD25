# McCulloh Pitts Not model
import numpy as np

def McNot(x,w,t):
    net = np.dot(x,w)
    if net>t:
        output = 1
    else:
        output = 0
    return output

x0 = np.array([0,1])
x1 = np.array([1,1])
w = np.array([-2,1])

t = 0
ans1 = McNot(x0,w,t)
print (x0, "value", ans1)
ans2 = McNot(x1,w,t)
print (x1, "value", ans2)
