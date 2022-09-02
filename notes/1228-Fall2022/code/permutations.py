
import copy

def nextPerm(arr):
    """
    Generates the next (ordered) permutation of the
    given elements (elements 0 thru n-1).

    """
    # 1. Find the right most pair such that a[i] < a[i+1]
    a = copy.deepcopy(arr)
    n = len(a)
    i = n-2
    while i >= 0 and a[i] >= a[i+1]:
        i -= 1
    if i < 0:
        return None
    # 2. Find the smallest element a' to the right of a[i] such that a[i] < a'
    indexOfMin = i + 1
    for j in range(i+1, n):
        if a[j] > a[i] and a[j] < a[indexOfMin]:
            indexOfMin = j
    # 3. Swap a[i], a' (indexOfMin)
    a[i], a[indexOfMin] = a[indexOfMin], a[i]
    # 4. Sort everything to the right of a'
    a[i+1:] = sorted(a[i+1:])
    return a


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
while arr is not None:
    #print(arr)
    arr = nextPerm(arr)
    count += 1
print("found ", count, " permutations")
