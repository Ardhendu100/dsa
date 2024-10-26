# Flipkart question
# Here pages of books and number of students are given.
# We need to minimize the maximum number of pages a student can read.
# Constraints - 
# 1) Same book can't read by 2 studnets
# 2) Each student atleast should have one book.
# 3) Book will be distributed in continues manner
# This question will work for both soted and unsorted array

a = [90, 20, 50, 40]   # Pages of books
k = 2    # Number of students

start = max(a) # max(a) beacaue atleast one studnet can read max pages of book
end = sum(a)
n = len(a)
result = -1


def is_valid(a, n, k, mid):
    student = 1
    s = 0
    for i in a:
        s = s + i
        if s > mid:
            student += 1
            s = i
        if student > k:
            return False
           
    return True
    
    
if (n < k):
    result = -1

else:
    while (start <= end):
        mid = start + (end-start)//2
        
        x = is_valid(a, n, k, mid)
        if x:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    
print(result)
        
