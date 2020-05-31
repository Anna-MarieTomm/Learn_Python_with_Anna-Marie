"""
fibonacci interative 

"""

#n = is the last value that should be presented 
def fibonacci_iterative (n-1):
    
    previous = 0
    current =1
    for i in range (n-1): 
        #note: a becomes b, and b becomes a+b 
        current_old  = current
        current = previous + current  
        previous = current_old 

    return (current)

print(fibonacci_iterative)

def fibonacci_recursive (n): 
    if n == 1: 
        return 1 
    else:
        return n
    
    return result

print (fibonacci_recursive (5))

