def factorial2(x):
    tot = 1
    i = x
    while i > 0:
        tot *= i
        i -= 1
    return tot
    
def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)
    
print 4
print factorial(4)
