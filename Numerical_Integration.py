# Trapezoidal Rule 


import math as m

def tr(fun,x0,xn,n):
    
     h = (xn-x0)/n
     print(h)
     yo = fun(x0)
     yn = fun(xn)
     
     yr = x0
     
     for i in range(1,n):
         yr = yr +fun(x0 + i * h)
    
     a = 0.5*h*(yo+yn+2*(yr))
     print ("Area Under Curve = %.4f"%a)
    



# Simpsons 1/3rd Rule

def sonethird(fun,xn,x0,n):
    
    h = (xn-x0)/n
    y0 = fun(x0)
    yn = fun(xn)
    
    yodd = 0 
    yeven = 0 
    
    for i in range(1,n,2):
        yodd = yodd + fun(x0+i*h)
    for j in range (2,n,2):
        yeven = yeven + fun(x0+i*h)
        
    A = (1/3)*h*(y0+yn+4*yodd+2*yeven)
    print("Area Under Curve =  %.4f"%A)
    
    
# Simpsons 3/8th Rule:
    
def simthreeeight(fun,xn,x0,n):
    
    h = (xn-x0)/n
    yo = fun(x0)
    yn = fun(xn)
    
    y3 = 0
    y2 = 0 
    
    for i in range(1,n,1):
        if i % 3 != 0:
           y3 = y3 + fun(x0+i*h)
        
    for j in range(1,n,3):
        y2 = y2 + fun(x0+i*h)
        
    A = (3/8)*h*(yo+yn+3*y3+2*y2)
    print(A)
    