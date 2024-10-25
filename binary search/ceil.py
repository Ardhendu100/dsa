# Find Ceil of an element in a Sorted Array
# we need to calculate smallest element greater the x
a = [1, 2, 3, 4, 8, 10, 10, 12, 19]
x = 5
result = -1
start = 0
end = len(a) - 1
while start <= end:
    mid = start + (end-start)//2
    if a[mid] == x:
        result = a[mid]
        break
    elif a[mid] > x:
        end = mid-1
        result = a[mid]
    else:
        start = start + 1
print(result)
        