a = [2,5,6,0,0,1,2]
n = len(a)
x = int(input("Enter the element to search: "))

def getMin():
    start = 0
    end = n - 1
    
    while start <= end:
        if a[start] <= a[end]:
            return start
        mid = start + ((end - start) // 2)
        next = (mid + 1) % n
        prev = (mid + (n-1)) % n
        
        if a[mid] <= a[next] and a[mid] <= a[prev]:
            return mid
        elif a[mid] >= a[start]:
            # Left side is sorted, go to the right side
            start = mid + 1
        else:
            # Right side is sorted, go to the left side
            end = mid - 1 

def findElement(arr, start, end):
    while start <= end:
        mid = start + ((end - start) // 2)
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
        
m = getMin()
if a[m] == x:
    print(f"Element {x} found at index {m}")
else:
    # Search in both halves of the array
    bsFirst = findElement(a, 0, m - 1)
    if bsFirst >= 0:
        print(f"Element {x} found at index {bsFirst}")
    else:
        bsLast = findElement(a, m + 1, n - 1)
        if bsLast >= 0:
            print(f"Element {x} found at index {bsLast}")
        else:
            print("Element not found")
