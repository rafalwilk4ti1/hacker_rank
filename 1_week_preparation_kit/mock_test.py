
arr = [0, 1, 2, 4, 6, 5, 3]

def findMedian(arr):
    arr.sort()
    median_number = len(arr) / 2
    if isinstance(median_number, float):
        median_number -= 0.5
    return arr[int(median_number)]



print(findMedian(arr))