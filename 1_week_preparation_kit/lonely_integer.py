a = [1, 2, 3, 4, 3, 2, 1]

def lonelyinteger(a):
    for x in a:
        if a.count(x) % 2 == 1:
            return x


print(lonelyinteger(a))