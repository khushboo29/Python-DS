#min and max of array 
def minimum(a):
    sorting(a)
    return a[0]
    
def maximum(a):
    sorting(a)
    return a[-1]

def sorting(a,s=0,e=5):
    if s<e:
        p = partition(a,s,e)
        sorting(a,s,p-1)
        sorting(a,p+1,e)

def partition(a,s,e):
    pivot = a[e]
    pIndex = (s-1)
    for i in range(s,e):
        if a[i]<=pivot:
            pIndex = pIndex+1
            a[i],a[pIndex] = a[pIndex],a[i]
    a[pIndex+1],a[e] = a[e],a[pIndex+1]
    return (pIndex+1)
    
#driver code 
a=[3,45,2,90,34,95]
#a=[2,3,34,45,90,95]
print(maximum(a))
print(minimum(a))

