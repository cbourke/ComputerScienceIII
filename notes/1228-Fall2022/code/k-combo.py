
import copy

def exploreAllCombos(set, currentSubset, i):
    """
    Given a set and a (current) subset of it and an index i
    this function explores the next subsets recursively by
    considering elements set[i+1] thru set[n-1]
    """
    n = len(set)
    if i >= n:
        #done
        return
    # TODO: process the current subset whatever "process" means
    print(currentSubset)
    # consider elements i+1 ... n-1 in set:
    #  add them to the subset and recurse
    for j in range(i+1, n):
        # add set[j] to currentSubset
        currentSubset.append(set[j])
        # recurse
        exploreAllCombos(set, currentSubset, j)
        # remove the last element (that was added) to set  yourself up
        # for the next loop...
        currentSubset.pop()


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
combo = [0, 1, 2, 3]
count = 0
exploreAllCombos(combo, [], -1)


# while combo is not None:
#     print(combo)
#     combo = nextCombo(combo, n)
#     count += 1
#
# msg = "found " + str(count) + " combos!"
# print("found ", count, " combos!")
# print(msg)
