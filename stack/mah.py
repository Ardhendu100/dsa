# Maximum Area of Histogram

a = [6, 2, 5, 4, 5, 1, 6]
stack = []
nsr = []
nsl = []


# For NSR
for i in range(len(a)-1, -1, -1):
    if len(stack) == 0:
        nsr.append(len(a))
    elif len(stack) > 0 and stack[::-1][0][0] < a[i]:
        nsr.append(stack[::-1][0][1])
    elif len(stack) > 0 and stack[::-1][0][0] >= a[i]:
        while(len(stack) > 0 and stack[::-1][0][0] >= a[i]):
            stack.pop()
        if(len(stack) == 0):
            nsr.append(len(a))
        else:
            nsr.append(stack[::-1][0][1])
    stack.append([a[i], i])
    
stack.clear()
nsr = nsr[::-1]

#For NSL

for i in range(0,len(a)):
    if len(stack) == 0:
        nsl.append(-1)
    elif len(stack) > 0 and stack[::-1][0][0] < a[i]:
        nsl.append(stack[::-1][0][1])
    elif len(stack) > 0 and stack[::-1][0][0] >= a[i]:
        while(len(stack) > 0 and stack[::-1][0][0] >= a[i]):
            stack.pop()
        if len(stack) == 0:
            nsl.append(-1)
        else:
            nsl.append(stack[::-1][0][1])
        
    stack.append([a[i], i])
    
print(nsr)
print(nsl)

# Formula to get width = (nsr-nsl)-1
width = [(nsr[i]-nsl[i])-1 for i in range(len(a))]
area = [width[i] * a[i] for i in range(len(a))]
print(max(area))
        