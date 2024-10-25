# Rain water Trapping

a = [3, 0, 0, 2, 0, 1]
size = len(a)    
# Initialize water, mxl (maximum on left), and mxr (maximum on right)
water = [0] * size
mxl = [0] * size
mxr = [0] * size
# maximum = max(a)

# Time complexity o(n2)
# for i in range(0, len(a)):
#     if (maximum == a[i]):
#         water.append(0)
#     else:
#         if (i == 0):
#             left = a[i]
#             right = maximum
#         else:
#             left = max(a[:i])
#             right = max(a[i:])
        
#         water.append(abs(a[i] - min(left, right)))
# print(sum(water))

mxl[0] = a[0]
mxr[size-1] = a[size - 1]
for i in range(1, size):
    mxl[i] = max(mxl[i-1], a[i])
    
for i in range(size - 2, -1, -1):
    mxr[i] = max(mxr[i+1], a[i])
    
for i in range(0, size):
    water[i] = abs(min(mxl[i], mxr[i]) - a[i])

print(sum(water))
print(mxl)
print(mxr)
print(water)