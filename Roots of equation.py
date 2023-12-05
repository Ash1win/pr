# Bisection Method

import math as m
def AAN_BSM(fun,x1,x2,itr,acc):
  while fun(x1)*fun(x2)> 0:
    print("Root does not lie in the given range, change hte intial guess")
    x1 = float(input("Enter new x1: "))
    x2 = float(input("Enter new x2: "))

    for i in range (1,itr):
      x0 = (x1+x2)/2
      if fun(x1)*fun(0)<0:
        x1 = x1
        x2 = x0
      elif fun(x1)*fun(0)>0:
        x1 = x0
        x2 = x2
      else:
        break

      if abs (x1-x0) <= acc:
        break
    print (f"The new root is{x0}")
    
    


# Newton Raphson Method

import math as m

def nrm (f,df,ddf,x0,maxitr,acc):
  while abs (f(x0)*ddf(x0)/df(x0)**2) > 1:
    print ("Intial guess is incorrect,provide new intial guess x0")
    x0 = input(float("Enter the value of new root: "))
  for i in range(maxitr):
    x1 = x0-(f(x0)/df(x0))
    if abs (x1-x0) >= acc:
      break
    else:
      x1 = x0
  print ("The root of given function is %.4f"%x1)
  
  
# Sucessive approximation method

import math as m
def sam (g,dg,x1,acc,maxitr):
  while abs (dg(x1)) > 1:
    print ("Intial guess is incorrect,provide new intial guess x0")
    x0 = input(float())
  for i in range(maxitr):
    x0 = g(x1)
    if abs (x1-x0) < acc:
      break
    else:
      x1 = x0
  print ("The root of given function is %.4f"%x0)

#sam(lambda x: (x**3+8)/15, lambda x: x**2/5,1, 0.001, 15)










import math as m

def BSM(fun,x1,x2,itr,accu):
    
  
    
    while fun(x1)*fun(x2) > 1:
        print("Intial gues is incorrect")
        x1 = float(input())
        x1 = float(input())
        
        
    for i in range(1,itr):
        
        x0 = (x1+x2)/2
        if fun(x0)*fun(x1)<0:
            x1 = x1
            x2 = x0
            
        elif fun(x0)*fun(x1)>0:
            x1 = x0
            x2 = x2 
            
        else:
            break
        
        if abs(x1-x0) <=  accu:
            break
        
    print (x0)    
        
    
        
        









