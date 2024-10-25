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
        print(stack)
    
    # Process the remaining items in the stack
    while stack:
        h = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * width)
    
    print(max_area)
    
heights = [2,1,5,6,2,3]
largestRectangleArea(heights)
