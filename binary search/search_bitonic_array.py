# Here we need to find the element in bitonic array
# bitonic array is like it increse regurlarly then decrese and so on
a = [1, 3, 8, 12, 4, 2]
x = int(input())


def peak_element(a):
    n = len(a)
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end-start)//2
        if mid > 0 and mid < n-1:
            if a[mid] > a[mid-1] and a[mid] > a[mid-1]:
                return mid
            elif a[mid-1] > a[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif mid == 0:
            return a.index(max(a[0], a[1]))
        elif mid == n-1:
            return a.index(max(a[mid], a[mid-1]))


def bs(arr, start, end):
    while start <= end:
        mid = start + ((end - start) // 2)
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def reversebs(arr, start, end):
    while start <= end:
        mid = start + ((end - start) // 2)
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1



p = peak_element(a)
if a[p] == x:
    print(p)
else:
    fbs = bs(a, 0, p)
    if fbs == -1:
        sbs = reversebs(a, p+1, len(a)-1)
        if sbs == -1:
            print("Not exist")
        else:
            print(sbs)
    else:
        print(fbs)
    
    
    