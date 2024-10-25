# Nearest greater to left

n = 4
a = [1,3,2,4]
vector = []
stack = []

for i in a:
    if len(stack) == 0:
        vector.append(-1)
    elif len(stack) > 0 and stack[-1] > i:
        vector.append(stack[-1])
    elif len(stack) > 0 and stack[-1] <= i:
        while len(stack) > 0 and stack[-1] <= i:
            stack.pop()
        if len(stack) == 0:
            vector.append(-1)
        else:
            vector.append(i)
    stack.append(i)
print(vector)

