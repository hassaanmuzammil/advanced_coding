from queue import LifoQueue

s = "[[([{(()}])]]"
def isBalanced(s):
    """
    :type s: str
    """
    stack = LifoQueue()
    idx = 0
    for c in s:
        if c in ['[','(','{']: 
            stack.put(c)
        else:
            if stack.empty():
                print("Bracket Mismatch at index: ",idx)
                return False
            top = stack.get()
            if top == '[' and c != ']' or top == '(' and c != ')' or top == '{' and c != '}':
                print("Bracket Mismatch at index: ",idx)
                return False
        idx += 1
    return stack.empty()


if __name__ == "__main__":
    s = "foobar(x);"
    
    # get brackets only
    brackets = []
    for c in s:
        if c in "[]{}()":
            brackets.append(c)
    brackets = ''.join(brackets)
    
    # run function
    isBalanced(brackets)
