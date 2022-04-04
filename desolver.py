from math import *
import matplotlib.pyplot as plt

# yp=yp+ypp
#y(0)=0
#yp(0)=3

t=0
y=0
yp=-7
graph=[]
#dt=.0000001
#n=500000
dt=.00001
ran=100000
ran=10
tl=[]

for i in range(ran):
    ypp=-11*yp-24*y
    print(ypp)
    yp=yp+ypp*dt
    y=y+yp*dt
    tl.append(t)
    t=t+dt
    graph.append(y)
    





plt.plot(tl,graph)
plt.show()
