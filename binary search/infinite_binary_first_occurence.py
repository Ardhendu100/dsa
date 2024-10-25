#  We need to find the first occurance of 1 in an inifinate array
# this problem is the combination of bs.py + firsoccurence.py +
# infinite_sorted_array.py

a = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
n = 1
result = -1


def bs(start, end):
    while (start <= end):
        mid = start + ((end-start) // 2)
        if a[mid] == n:
            result = mid
            end = mid - 1
        elif n < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result


start = 0
end = 1

while (a[end] < n):
    start = end
    end = end * 2

res = bs(start, end)
print(res)