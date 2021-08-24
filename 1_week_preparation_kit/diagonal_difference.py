arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]


def diagonalDifference(arr):
    sum_left_to_right = 0  # arr[0][0] + arr[1][1] + arr[2][2]
    sum_right_to_left = 0  # arr[0][2] + arr[1][1] + arr[2][0]
    i = 0
    j = 0
    k = 0
    l = len(arr) - 1
    for y in range(len(arr)):
        sum_left_to_right += arr[i][j]
        sum_right_to_left += arr[k][l]
        i += 1
        j += 1
        k += 1
        l -= 1
    return abs((sum_left_to_right - sum_right_to_left))

print(diagonalDifference(arr))
