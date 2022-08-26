
letters = "abcdefghijklmnopqrstuvwxyz"
list = [*letters]
n = len(list)

for i in range(2**n):
    bin = format(i, 'b')
    # pad out with leading zeros...
    while len(bin) < n:
        bin = "0" + bin
    print(f"{i}, {bin}")
    # build the subset...
    subset = []
    for j in range(len(bin)):
        if bin[j] == "1":
            subset.append(list[j])
    print(subset)
