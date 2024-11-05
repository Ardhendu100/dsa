n = int(input())


def factorial(n, result):
    if n == 1:
        result *= 1
        return result
    
    result *= n 
    return factorial(n-1, result)
    
    
result = 1
res = factorial(n, result)
print(res)
    