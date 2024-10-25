a = [20, 17, 15, 14, 12, 7, 4]

n = int(input())  # we need to find the position of n value
start = 0
end = len(a)-1

while (start <= end):
    mid = start + ((end-start) // 2)
    if a[mid] == n:
        print(mid)
        break
    elif n < a[mid]:
        start = mid + 1
    else:
        end = mid - 1
        
