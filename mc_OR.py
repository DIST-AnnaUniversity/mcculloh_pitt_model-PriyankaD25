#McCulloh Pitts OR Model
import numpy as np

def McOR(x,w,t):
    net = np.dot(x,w)
    if net>t:
        output = 1
    else:
        output = 0
    return output

x0 = np.array([0,0,1])
x1 = np.array([0,1,1])
x2 = np.array([1,0,1])
x3 = np.array([1,1,1])
w = np.array([2,2,-1])

t = 0
ans1 = McOR(x0,w,t)
print (x0, "value", ans1)
ans2 = McOR(x1,w,t)
print (x1, "value", ans2)
ans3 = McOR(x2,w,t)
print (x2, "value", ans3)
ans4 = McOR(x3,w,t)
print (x3, "value", ans4)
