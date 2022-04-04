from math import *
import time
import matplotlib.pyplot as plt

def linspace(start,end,N):
    a=start
    b=end
    n=N
    q=(b-a)/n
    cont=1
    u=a
    x=[]
    while cont==1:
        x.append(round(u,len(str(N))+1))
        u+=q
        if u>b and q>0:
            cont=0
        if u<b and q<0:
            cont=0
    return x

def rsolve(equation,var):
    eq=equation.split("=")
    left=str(eq[0])
    right=str(eq[1])
    right="-1*("+right+")"
    expr=left+right
    expr=expr.replace(var,"x[k]")
    spot=0
    maxx=1000
    for j in range(10):
        x=linspace(spot-maxx/10**j,spot+maxx/10**j,100)
        y=[]
        try:
            for k in range(len(x)):
                y.append(abs(eval(expr)))
        except:
            print("error")
        minn=10**200
        for i in range(len(y)):
            if y[i]<minn:
                minn=y[i]
                spot=x[i]
    return x[50]


#y'=y'+y''
#y(0)=0
#y'(0)=3


def desolve(equation,tf,order):
    t=0 #initial value time
    ylist=[]
    for i in range(order):
        use="y"+str(i)
        string="enter y"+str(i)+" value: "
        use="float(input(string))"
        use=eval(use)
        ylist.append(use)

    graph=[] #graph later
    dt=.001
    tlist=[]

    
    hi="y"+str(order)
    eq=equation
    runs=500000
    runs=100
    runs=tf/dt
    print("total needed iterations: ",runs)
    ti=time.time()
    for i in range(round(runs)):
        if (100*i/runs)%2==0: #2 percents
            print((100*i/runs),"percent")
         
        if i==0:
            for j in range(order): #replace y0 y1 with ylist values
                eq=eval("eq.replace(\"y"+str(j)+"\",str(ylist[j]))")
                
            eq=eq.replace("t",str(t))
            ylist.append(rsolve(eq,hi))#solve for highest order
            
            ylistog=[] #create delayed ylist variable
            for j in range(len(ylist)):
                ylistog.append(ylist[j])

            #initial time estimate
            mins=runs/60 * (time.time()-ti)
            print("initial time estimate: ",round(mins,3),"minutes")


            
        if i>0:
            for j in range(order):
                #replace og ylist value with updated value
                eq=eq.replace(str(ylistog[j]),str(ylist[j]))
            print(t)
            eq=eq.replace("t",str(t))

            for j in range(len(ylist)): #update delayed ylist
                ylistog[j]=ylist[j]

            ylist[len(ylist)-1]=rsolve(eq,hi) #solve for highest order

        for j in range(order): #v+=a*dt
            ylist[order-j-1]=ylist[order-j-1]+ylist[order-j]*dt

        tlist.append(t)
        t=t+dt
        graph.append(ylist[0])

    plt.plot(tlist,graph)
    plt.show()
    print("estimate at t =",tf,":",graph[len(graph)-1])


desolve("y2=-11*y1-24*y0*t",.1,2)
