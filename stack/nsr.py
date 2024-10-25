# Nearest smaller to left
n = 5
a = [4,5,2,10,8]
vector = []
stack = []

for i in a[::-1]:
    if len(stack) == 0:
        vector.append(-1)
    elif len(stack) > 0 and stack[-1] < i:
        vector.append(stack[-1])
    elif len(stack) > 0 and stack[-1] >= i:
        while len(stack) > 0 and stack[-1] >= i:
            stack.pop()
        if len(stack) == 0:
            vector.append(-1)
        else:
            vector.append(stack[-1])
    stack.append(i)
print(vector[::-1])