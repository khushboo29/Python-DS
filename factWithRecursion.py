#factorial
#recursive
def factorial(n):
    if n==0:
        return
    if n==1:
        return 1 
    if n>1:
        return(n*factorial(n-1))

#iterative       
def factorial(n):
    res=1
    if n<0:
        return
    if n==1:
        return 1 
    for i in range(2,n+1):
        res=res*i
    return res
        
r=factorial(5)
print(r)
