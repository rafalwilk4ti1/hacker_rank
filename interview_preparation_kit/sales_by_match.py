from collections import Counter


def sockMerchant(n, ar):
    counter = Counter(ar)
    count = 0
    for x in counter.values():
        if x % 2 ==0:
            count += x//2
        elif x >= 2:
            count += x//2
        else:
            continue

    return count