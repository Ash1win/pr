# Straight Line
import math as m
import numpy as np
def sl(x,y):
    
    x = x.astype(float)
    y = y.astype(float)
    
    a = np.array([[len(x),sum(x)],
                  [sum(x),sum(x**2)]])
    
    d = np.array([[sum(y)],
                  [sum(x*y)]])
    
    b = np.linalg.solve(a, d)
    
    
    print("y = %.4f + (%.4f) * x"%(b[0],b[1]))
    


# Parabolic Equation

def par(x,y):
    
    x = x.astype(float)
    y = y.astype(float)
    
    a = np.array([[len(x),sum(x),sum(x**2)],
                  [sum(x),sum(x**2),sum(x**3)],
                  [sum(x**2),sum(x**3),sum(x**4)]])
    
    d = np.array([[sum(y)],
                  [sum(x*y)],
                  [sum(x**2*y)]])
    
    b = np.linalg.solve(a, d)
    
    print("y = %.4f + (%.4f) * x + (%.4f) * x**2"%(b[0],b[1],b[2]))
    
    
# Power equation

def pe(x,y):
    
    x = x.astype(float)
    y = y.astype(float)
    
    e = np.log(x)
    f = np.log(y)
    
    a = np.array([[len(x),sum(e)],
                  [sum(e),sum(e**2)],
                  ])
    
    d = np.array([[sum(f)],
                 [sum(e*f)]])
    
    
    b = np.linalg.solve(a, d)
    
    alpha = m.exp(b[0])
    
    beta = b[1] 
    
    print("y = %.4f * x ^ %.4f"%(alpha,beta))