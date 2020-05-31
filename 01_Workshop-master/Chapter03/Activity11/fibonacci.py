def fibonacci_iterative(n):
    previous = 0
    current = 1
    for i in range(n - 1):
        current_old = current
        current = previous + current
        previous = current_old
    return current


def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)

    
    
    
stored_results = {}

def fibonacci_dynamic(n): 
 
    for i in reversed(range(n)): 
        if i +1 in stored_results: 
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_result[i+1]
            break
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)
    
    
    
