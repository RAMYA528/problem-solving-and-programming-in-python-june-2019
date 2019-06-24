#Function to check prime or not
def isprime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if count==2:
        return True
    else:
        return False
    
    
#function to determine number of primefactors
def numberofprimefactors(n):
    if isprime(n):
        return 1
    count=0
    for i in range(2,n//2+1):
        if isprime(i) and n%i==0:
            count+=1
    return count
