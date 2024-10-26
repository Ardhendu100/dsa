#  In this problem we need to find the peak value
a = [1, 3, 8, 12, 4, 2]


def peak_element(a):
    n = len(a)-1 
    start = 0
    end = n 
    if (len(a) == 1):
        return 0
    while (start <= end):
        mid = start + (end-start)//2
        
        if mid > 0 and mid < n:
            if a[mid] > a[mid-1] and a[mid] > a[mid + 1]:
                return mid
            elif a[mid-1] > a[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif mid == 0:
            return a.index(max(a[mid], a[mid+1]))
        elif mid == n:
            
            return a.index(max(a[mid], a[mid-1]))
     
        
x = peak_element(a)
print(x)