# Here we will search value in a 2d array where it is sorted row ise and column wise
# Time complexity (n+m)
a = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 47],
    [32, 33, 39, 50]
]
n = 4
m = 4
k = int(input())
result = []
# first we will start from a[0][3] top right corner

i = 0
j = m-1

while (i >= 0 and i < n and j >= 0 and j < m):
    if a[i][j] == k:
        result.append(i)
        result.append(j)
        break
    elif a[i][j] > k:
        j -= 1
    elif a[i][j] < k:
        i += 1


if (len(result) == 2):
    print(result)
else:
    print(-1)
    