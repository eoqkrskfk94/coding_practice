def solution(s):
    
    count = 0
    stack = []
    stack2= []
    for i in s:
        if i == '(':
            stack.append('(')
        if i == ')':
            stack2.append(')')
            if len(stack) != 0:
                stack.pop()
                stack2.pop()

    print(stack2)
    
    if len(stack) == 0 and len(stack2) == 0:
        return True
    else:
        return False
