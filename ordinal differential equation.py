# Euler's Method

def em(fun,x0,y0,xn,n):
    
    h = (xn-x0)/n
    
    for i in range(1,n+1):
        ynew = y0 + h*fun(x0,y0)
        x0 =x0+h
        y0 = ynew
        print("X = %.4f"%x0, "Y = %.4f"%y0)




#Runge Kutta 2nd order

def rk2(fun,x0,y0,xn,n):
    
    h = (xn-x0)/n
    
    for i in range(1,n+1):
        k1 = h*fun(x0,y0)
        k2 = h*fun(x0+h,y0+k1)
        x0 = x0+h
        ynew = y0+0.5*(k1+k2)
        y0 = ynew
        
        print("X = %.4f"%x0,"K1 = %.4f"%k1,"Y = %.4f"%y0)
        
    
        
 
        
        
    

