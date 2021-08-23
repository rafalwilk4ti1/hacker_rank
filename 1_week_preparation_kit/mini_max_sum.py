

arr = [1, 3, 5, 7, 9]

def miniMaxSum(arr):
    arr.sort()
    min_num = sum(arr[0:4])
    max_num = sum(arr[1::])
    print(min_num, max_num)

print(miniMaxSum(arr))