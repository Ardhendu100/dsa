# We have to calculate next aphabet elemet

a = ['a', 'c', 'd', 'f', 'i', 'k', 'm']
n = len(a)
start = 0
end = n-1
res = -1
x = input()

while start <= end:
    mid = start + (end-start)//2
    if a[mid] == x and mid < n - 1:
        res = a[mid+1]
        break
    elif ord(a[mid]) > ord(x):
        res = a[mid]
        end = end - 1
    else:
        start = start + 1
print(res)
        
    
