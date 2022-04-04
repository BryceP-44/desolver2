from math import *
import matplotlib.pyplot as plt

# y'' + 11y' = -24y
#y(0)=0
#yp(0)=-7

t=0 #initial time
y=0 #initial y
yp=-7 #initial y'
tf=5 #final time

graph=[]
rang=10000 #total number of points
dt=(tf-t)/rang
tl=[]

for i in range(rang):
    ypp=-11*yp-24*y #solve for highest order (do on paper first)
    yp+=ypp*dt #adjust all y values less than highest order
    y+=yp*dt #adjust
    tl.append(t) 
    t=t+dt #increment time
    graph.append(y)
    

print("estimate at t =",round(t,3),"is:",graph[len(graph)-1])



plt.plot(tl,graph)
plt.show()
