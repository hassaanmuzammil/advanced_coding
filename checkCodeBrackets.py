def check_brackets_only(s):
    """
    :type s: str
    """
    
    stack = []
    for i,c in enumerate(s):
        if c in '({[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False, i + 1
            
            top = stack.pop(-1)    
            if (top == '[' and c != ']') or (top == '(' and c != ')') or (top == '{' and c != '}'):
                return False, i + 1
        
    if len(stack) == 0:
        return True, -1
    else:
        return False, i + 1
    
def get_brackets_indices(s):
    indices = []
    for i,c in enumerate(s):
        if c in '[](){}':
            indices.append(i)
    return indices

def get_brackets_only(s):
    brackets = []
    for c in s:
        if c in '[](){}':
            brackets.append(c)
    return ''.join(brackets)

def check_code_brackets(s):
    b = get_brackets_only(s)
    idx = get_brackets_indices(s)
    ans, i = check_brackets_only(b)
    #print(s, b, idx, ans, i)
    if ans == True:
        return "Success"
    else:
        return idx[i-1]

"""
s = 'foobar(x[i)'
check_code_brackets(s)
#returns 10

s = "col = [char for char in s_copy[0:numRows]]"
check_code_brackets(s)
#returns 'Success'
"""
