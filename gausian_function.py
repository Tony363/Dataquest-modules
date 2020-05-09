import math
import numpy as np

def gauss(x, n, m=0, s=1):
    f = 1/math.sqrt((2*math.pi))*math.e**(-.5*((x-m)/s)**2)
    f1 = 1/math.sqrt((2*math.pi))*math.e**(-.5*(((x-5*s)-m)/s)**2) 
    f2 = 1/math.sqrt((2*math.pi))*math.e**(-.5*((x-(m + 5*s))/s)**2)
    array = [i for i in np.linspace(f1,f2,5)]
    return array

print(gauss(2,5))