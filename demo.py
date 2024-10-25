stack = []
nums = [-2,1,2,-2,1,2]
m = nums[-1]
flag = 0
for i in range(len(nums)-1, -1, -1):
    print(i, stack)
    
    if (len(stack) == 0):
        stack.append(nums[i])
    elif len(stack) == 1 and nums[i] > stack[-1]:
        stack.append(nums[i])
    elif len(stack) >= 2:
        
        if (nums[i] < stack[-2] or nums[i] < stack[0]):
            # print('---')
            print(True)
        elif any(a > nums[i] for a in stack[:-1]):
            # print('---', nums[:-1])
            print(True)
        elif nums[i] > stack[-1]:
            stack.append(nums[i])
    else:
        if (min(m, nums[i]) == m and m != nums[i]):
            stack = []
            stack.append(m)
            stack.append(nums[i])
            m = min(m, nums[i])
        m = min(m, nums[i])
        if (nums[i] not in stack and flag == 1):
            stack.insert(0, nums[i])
        print('m', m)
print(False)



# class Solution(object):
#     def find132pattern(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         stack = []
#         m = nums[-1]
#         flag = 0
#         for i in range(len(nums)-1 , -1, -1):
#             if(len(stack) == 0):
#                 stack.append(nums[i])
#             elif len(stack) == 1 and nums[i] > stack[-1]:
#                 stack.append(nums[i])
#             elif len(stack) >= 2:
                
#                 if(nums[i] < stack[-2] or nums[i] < stack[0]):
#                     return True
#                 elif any(a > nums[i] for a in stack[:-1]):
#                     return True
#                 elif nums[i] > stack[-1]:
#                     stack.append(nums[i])
#             else:
                
#                 if(min(m, nums[i]) == m and m!= nums[i]):
#                     flag = 1
#                     stack = []
#                     stack.append(m)
#                     stack.append(nums[i])
#                     m = min(m, nums[i])
#                 m = min(m, nums[i])
#                 if(nums[i] not in stack and flag == 1):
#                     stack.insert(0, nums[i])
                    
#         return False

                       
      
