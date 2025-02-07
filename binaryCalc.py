def add_binary(a, b):
    n = a + b  
    binary_num = "" 
    
    if n == 0:
        return "0"  # Special case if the sum is 0
    
    while n > 0:
        binary_num = str(n % 2) + binary_num  # Get remainder (0 or 1) and add it to the front
        n = n // 2  
    
    return binary_num  