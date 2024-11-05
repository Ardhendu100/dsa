# print 1 to n / n to 1

def oneToN(n):
    
    if n == 1:   # Base condition
        print(1)
        return True
    oneToN(n-1)   #hypothesis -> what we design
    
    print(n)     # induction
 
    
oneToN(7)
print("--------------")


def nToOne(n):
    
    if n == 1:   # Base condition
        print(1)
        return True
    print(n)     # induction
    
    nToOne(n-1)   #hypothesis -> what we design
    
 
    
nToOne(7)
    
    