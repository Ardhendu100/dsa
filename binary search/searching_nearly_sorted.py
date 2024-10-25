# Searching in a nearly sorted array

a = [5, 10, 30, 20, 40]
n = len(a)
start = 0
end = n - 1
x = int(input())

while start <= end:
    mid = start + (end-start)//2
    if a[mid] == x:
        print(mid)
        break
    elif mid-1 >= start and a[mid-1] == x:
        print(mid-1)
        break
    elif mid+1 <= end and a[mid+1] == x:
        print(mid+1)
        break
    elif a[mid-1] > x:
        end = mid - 2
    else:
        start = mid + 2
    