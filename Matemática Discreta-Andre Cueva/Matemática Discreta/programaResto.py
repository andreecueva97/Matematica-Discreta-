import math

def euclides(a,b):
    
    if(b == 0):
        return a
    else:
        return(euclides(b,a%b))

def combinacionLineal(a,b):
    
    if( b == 0):
        return (1,0)
    else:
        
        r = a%b
        q = a//b
        
        return( combinacionLineal(b,r)[1], combinacionLineal(b,r)[0] - combinacionLineal(b,r)[1] * q )