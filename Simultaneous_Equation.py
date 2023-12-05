# Gauss Elimination method

import numpy as np

def gem(a,d):
    
    a = np.array(a,dtype = float)
    d = np.array(d,dtype = float)
    n = len(d)
    print(n)
    
    for i in range(0,n,1): # i = 0
        for k in range(i+1,n,1): # i+1= 0+1 = k = 1
            fact = a[k,i]/a[i,i] # a[1,0]/a [0,0] = 3/4
            for j in range (0,n,1): # j = 0
                a[k,j] = a[k,j] - fact *a[i,j] # a[1,0] - fact * a[0,0]
                d[k] = d[k] - (fact * d[j]) # d[0] - fact * d[1]
                
    
    print("Upper Triangular Matrix = ")
    print(a)
    
    print("Constant Vectors = ")
    print(d)
                 
    x = np.zeros(n)
    for i in range (n-1,-1,-1):
        temp = 0
        
        for j in range(i+1,n,1):
            temp = temp + a[i,j]*x[j]
        x[i] = (d[i]-temp)/a[i,i]
        for i in range(n):
           print("x(%i) = %.4f"%(i,x[i]))

            
# Gauss Siedal Method

a = np.array([[4,1,2,3],[3,4,1,2],[2,3,4,1],[1,2,3,4]])
d = np.array([40,40,40,40])

a = np.array(a,dtype=float)
d = np.array(d,dtype = float)

n = len(d)
print ("Number of equation = ",n)
maxitr = 6
x = np.zeros(n)

for itr in range(0,maxitr,1):
    for i in range(0,n,1):
        temp = 0
        for j in range(0,n,1):
            if i != j:
                temp = temp + a[i,j] * x[j]
        x[i] = (d[i]-temp)/a[i,i]
for i in range(0,n,1):
    print("New roots %.4f"%x[i])

        