# Count of an Element in a sorted array
# to ge result we need to calculate last occurance - first occurance  + 1
a = [2, 4, 10, 10, 10, 18, 20]
n = 10

# print(a.count(n))

# last occurance
result = -1


def last_occurance(a):
    start = 0
    end = len(a)-1
    result = -1

    while (start <= end):
        mid = start + ((end-start) // 2)
        if a[mid] == n:
            result = mid
            start = mid + 1
        elif n < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result


def first_occurance(a):
    start = 0
    end = len(a)-1
    result = -1

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


last = last_occurance(a)
first = first_occurance(a)
c = (last - first) + 1
print(c)