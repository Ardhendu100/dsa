# Nearest greater to right
#  If j depends upon i then do stack
# n = int(input("Enter number of elements : "))
# a = list(map(int, input().strip().split()))[:n]

n = 4
a = [1,3,2,4]
vector = []
stack = []

for i in a[::-1]:
    if(len(stack) == 0):
        vector.append(-1)
    elif(len(stack) > 0 and stack[-1] > i):
        vector.append(stack[-1])
    elif(len(stack) > 0 and stack[-1] <= i):
        while len(stack) > 0 and stack[-1] <= i:
            stack.pop()
        if(len(stack) == 0):
            vector.append(-1)
        else:
            vector.append(stack[-1])

    stack.append(i)
print(vector[::-1])


