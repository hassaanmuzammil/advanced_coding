def number_of_digits(n):
    num_digits = 0
    while n != 0:
        n = n // 10
        num_digits += 1
        
    return num_digits
  
def is_narcissistic(value):
    num_digits = number_of_digits(value)
    str_value = str(value)
    sum = 0
    for i in range(num_digits):
        sum += int(str_value[i]) ** num_digits
        
    return sum == value
    
