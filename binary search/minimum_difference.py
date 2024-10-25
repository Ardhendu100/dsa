# we need to calculate the minimum diff of soreted array
a = [1, 2, 3, 4, 8, 10, 12, 19]

x = int(input())
n = len(a)
start = 0
end = n - 1
result = -1
while (start <= end):
    mid = start + (end-start)//2
    if a[mid] == x:
        result = 0
        print(0)
        break
    elif x < a[mid]:
        end = mid - 1
    else:
        start = mid + 1

if result != 0:
    # Make sure start doesn't go beyond array bounds
    if start >= n:
        start = n - 1
    # Make sure end doesn't go below 0
    if end < 0:
        end = 0
        
    diff1 = abs(x - a[start])
    diff2 = abs(x - a[end])
    print(min(diff1, diff2))
