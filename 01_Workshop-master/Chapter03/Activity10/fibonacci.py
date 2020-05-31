def fibonoacci_iterative (n): 
        a = 0
        b = 1
        
    for i in range(n-1): 
        old_a = a 
        a = b
        b = b+old_a
        
    return a

print(fibonacci_iterative) 