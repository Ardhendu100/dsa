# Here we need to find number of times sorted array is rotated
# number of times sorted array is rotated =  index of min element

# a = [11, 12, 15, 18, 2, 5, 6, 8]
a = [18, 2, 5, 6, 8, 11, 12, 15]
# a = [5, 2, 3]
start = 0
end = len(a) - 1

if len(a) == 1:
    print(0)

else:
    while (start <= end):
        mid = start + ((end-start) // 2)
        next = (mid+1) % len(a) 
        prev = (mid + (len(a)-1)) % len(a) 
    
        if a[mid] <= a[next] and a[mid] < a[prev]:
            print(mid)
            break
        elif a[start] <= a[mid] and a[mid] <= a[end]:
            end = mid-1
        elif a[start] >= a[mid] and a[mid] <= a[end]:
            end = mid-1
        else:
            start = mid + 1
    
