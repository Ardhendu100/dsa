# we have to fine the position of x in infinite sorted array
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 22, 26, 28, 30]
n = int(input())


def bs(start, end):
    while (start <= end):
        mid = start + ((end-start) // 2)
        if a[mid] == n:
            return mid
        elif n < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
 
         
start = 0
end = 1

while (a[end] <= n):
    start = end
    end = end * 2

result = bs(start, end)
print(result)