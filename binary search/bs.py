a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input())  # we need to find the position of n value
start = 0
end = len(a)-1

while (start <= end):
    mid = start + ((end-start) // 2)
    if a[mid] == n:
        print(mid)
        break
    elif n < a[mid]:
        end = mid - 1
    else:
        start = mid + 1
    
