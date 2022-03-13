#Find GCD or HCF of two numbers x and y
def gcd(x,y):
    small = x if x<y else y
    for i in range(1,x+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd

#test
print(gcd(24,54))
