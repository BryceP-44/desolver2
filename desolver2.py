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
    for j in range(5):
        x=linspace(spot-maxx/10**j,spot+maxx/10**j,100)
        y=[]
        try:
            for k in range(len(x)):
                y.append(abs(eval(expr)))
        except Exception as z:
            #print("error:",z)
            z=1
            
        minn=10**200
        for i in range(len(y)):
            if y[i]<minn:
                minn=y[i]
                spot=x[i]
    return x[50]


#y'=y'+y''
#y(0)=0
#y'(0)=3

dd=10**-300


def desolve(equation,tf,order):
    
    ylist=[]
    t=float(input("Enter initial time: ")) #initial time value
    t=t+dd
    for i in range(order):
        string="Enter y"+str(i)+" value: "
        use="float(input(string))"
        use=eval(use)
        ylist.append(use)

    graph=[] #graph points later
    tlist=[] #also for graph later

    
    hi="y"+str(order)
    eq=equation
    
    dt=.01
    runs=(tf-t)/dt
    print("Required amount of iterations:",round(runs))
    
    ti=time.time()
    for i in range(round(runs)):
        if i%200==0: #2 percents
            print(round(100*i/runs),"percent")
         
        if i==0:
            for j in range(order): #replace y0 y1 with ylist values
                eq=eval("eq.replace(\"y"+str(j)+"\",str(ylist[j]))")
                
            eq=eq.replace("t",str(t))
            ylist.append(rsolve(eq,hi))#solve for highest order
            
            ylistog=[] #create delayed ylist variable
            for j in range(len(ylist)):
                ylistog.append(ylist[j])

            tog=t

            #initial time estimate
            mins=runs/60 * (time.time()-ti)
            print("Initial runtime estimate: ",round(mins,3),"minutes")


            
        if i>0:
            for j in range(order):
                #replace og ylist value with updated value
                eq=eq.replace(str(ylistog[j]),str(ylist[j]))

            eq=eq.replace(str(tog),str(t))
            tog=t
            #print(t)

            for j in range(len(ylist)): #update delayed ylist
                ylistog[j]=ylist[j]

            ylist[len(ylist)-1]=rsolve(eq,hi) #solve for highest order
            #print(eq)

        for j in range(order): #v+=a*dt
            ylist[order-j-1]=ylist[order-j-1]+ylist[order-j]*dt #error

        tlist.append(t)
        t=t+dt
        graph.append(ylist[0])

    print("estimate at t =",tf,":",graph[len(graph)-1])
    plt.plot(tlist,graph)
    plt.show()
    
    


desolve("y1=cos(t)",10,1)
