# Stock Span Problem
# In this problem basically 7 days stocks rate are visible, we need to find the count of consecutive smaller or equal to before current day. For each day we need to check.
a = [100,80,60,70,60,75,85]
vector = []
stack = []

for i in range(0,len(a)):
   
    if len(stack) == 0:
        vector.append(i-(-1))
    elif len(stack) > 0 and stack[::-1][0][0] > a[i]:
        vector.append(i- (stack[::-1][0][1]))
    elif len(stack) > 0 and stack[::-1][0][0] <= a[i]:
        while(len(stack) > 0 and stack[::-1][0][0] <= a[i]):
            stack.pop()
        if len(stack) == 0:
            vector.append(i-(-1))
        else:
            vector.append(i-(stack[::-1][0][1]))
            
    stack.append([a[i], i])
   
print(vector)
