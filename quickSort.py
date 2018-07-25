#quicksort python implementation
##pseudocode
#quicksort(A,start,end)
#if(start<end)
#partition(A,start,end)
#quicksort(A,start,pIndex-1)
#quicksort(A,pIndex+1,end)
#
#partition(A,start,end)
#pivot = A[end]
#pIndex = (start-1)
#for(0 to end-1)
#{if(A[i]<=pivot)
#swap A[i],A[pIndex]
#pIndex = pIndex+1
#}
#swap A[pIndex+1],A[end]
#return (pIndex+1)

def quicksort(A,start,end):
    if(start<end):
        pIndex = partition(A,start,end)
        quicksort(A,start,pIndex-1)
        quicksort(A,pIndex+1,end)
        
def partition(A,start,end):
    pivot = A[end]
    pIndex = (start -1)
    for i in range(start,end):
        if A[i]<=pivot:
            pIndex = pIndex+1 
            A[i],A[pIndex] = A[pIndex],A[i]
        
    A[pIndex+1],A[end] = A[end],A[pIndex+1]
    return (pIndex+1)
    
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr,0,n-1)
print ("Sorted array is:"),
for i in range(n):
    print ("%d" %arr[i]),
    
