# Maximum area of rectangle in binary matrix
# arr = [
#     [0, 1, 1, 0],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 0, 0]
# ]
arr = [
    [0, 1],
    [0, 1]
]
n = 2
m = 2
maxA = 0
vector = []


def largestRectangleArea(heights):
    stack = []
    max_area = 0
    n = len(heights)
    
    for i in range(n):
        # Process each element while maintaining a monotonically increasing stack
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)
    
    # Process the remaining items in the stack
    while stack:
        h = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * width)
    print(max_area)
    return (max_area)


for i in range(0, n):
    for j in range(0, m):
        if (i == 0):
            vector.append(arr[i][j])
        else:
            if (arr[i][j] == 0):
                vector[j] = 0
            else:
                vector[j] = vector[j] + arr[i][j]
    d = largestRectangleArea(vector)
    if (d > maxA):
        maxA = d
print(maxA)
    