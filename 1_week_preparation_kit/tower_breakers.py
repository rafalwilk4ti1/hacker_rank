n = 1
m = 4


def towerBreakers(n, m):
    if m==1 or n%2==0:
        return 2
    else:
        return 1
print(towerBreakers(n, m))