import numpy as np

np.random.seed(0)



def h(x,p):
    return X**p
def f(x):
    return 1/2*np.exp(-abs(x))
def g(x):
    return (1/(2 * np.sqrt(2 * np.pi))) * np.exp((-1/2) * (x/2)**2)



    
Number_of_samples = [100,500,1000]
EXvalues = [1,2,5]
for j in EXvalues:
    print('E(X^p) where p is ',j)
    for i in Number_of_samples:
        print("For Value of N = ",i)
        X = np.random.normal(0,scale=2,size=i)
        value = 1/i * np.sum(h(X,j)*f(X)/g(X))
        if(j%2 == 1):
            value2 = 0
        else:  
            value2 = 2 #E(X**2)
        print("Using importance Sampling ",value,"\nActual ",value2,"\nError ",abs(value-value2));
