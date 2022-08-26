
import copy


def nextCombo(combo, n):
    """
    Given a current k-combination of integers 0 thru n-1,
    this function produces a *new* list representing the
    next k-combination.

    Returns None when no more combinations are possible
    """
    result = copy.deepcopy(combo)
    k = len(combo)
    # find the last element such that element != n - k + i
    i = k - 1
    while i >= 0 and result[i] == n - k + i:
        i -= 1
    if i < 0:
        # no next combination...
        return None
    # the element at i needs to be replaced with a[i] + 1
    result[i] += 1
    for j in range(i + 1, k):
        #replace result[j] with result[i] + j - i
        result[j] = result[i] + j - i
    return result


n = 4
k = 2
combo = [0, 1]
count = 0

while combo is not None:
    print(combo)
    combo = nextCombo(combo, n)
    count += 1

msg = "found " + str(count) + " combos!"
print("found ", count, " combos!")
print(msg)
