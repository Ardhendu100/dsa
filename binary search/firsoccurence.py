a = [2, 4, 10, 10, 10, 18, 20]
n = 10  # we need to find the first occurance of 10

start = 0
end = len(a)-1
result = -1

# # first occurance
while (start <= end):
    mid = start + ((end-start) // 2)
    if a[mid] == n:
        result = mid
        end = mid - 1
    elif n < a[mid]:
        end = mid - 1
    else:
        start = mid + 1
print(result)

# last occurance

# while (start <= end):
#     mid = start + ((end-start) // 2)
#     if a[mid] == n:
#         result = mid
#         start = mid + 1
#     elif n < a[mid]:
#         end = mid - 1
#     else:
#         start = mid + 1
# print(result)
         
