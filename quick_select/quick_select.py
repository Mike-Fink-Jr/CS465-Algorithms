import sys
from random import randrange

def partition(x, pivot_index):
    i = 0
    if pivot_index !=0:
        x[i],x[pivot_index] = x[pivot_index],x[i]

    for n in range(len(x)-1): #bulk partion
        if x[n+1] < x[0]:
            x[n+1],x[i+1] = x[i+1],x[n+1]
            i += 1

    x[0],x[i] = x[i],x[0] # swap back
    return x,i

def quickSelect(arr,k):
    if len(arr) == 1:
        return arr[0]
    else:
        partitioned_arr = partition(arr,randrange(len(arr)))
        arr = partitioned_arr[0] # partitioned array
        j = partitioned_arr[1] # pivot index
        if j == k:
            return arr[j]
        elif j > k:
            return quickSelect(arr[:j],k)
        else:
            k = k - j - 1
            return quickSelect(arr[(j+1):], k)

# Read input
test_values = [int(x) for x in sys.stdin.readline().split()]
n = test_values[0]
k = test_values[1]
numbers = [int(x) for x in sys.stdin.readline().split()]

kSmallest = quickSelect(numbers,k)

print kSmallest