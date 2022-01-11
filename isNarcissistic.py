def is_narcissistic(value):
    
    str_value = str(value)
    num_digits = len(str_value)
    sum = 0
    
    for i in range(num_digits):
        sum += int(str_value[i]) ** num_digits
        
    return sum == value
 
