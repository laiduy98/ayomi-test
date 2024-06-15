# Resolve a npi expression
def npi(expression):
    stack = []
    ops = {'+', '-', '*', '/'}
    
    print(expression.split())
    for item in expression.split():
        if item in ops:
            b = stack.pop()
            a = stack.pop()
            match item:
                case '+':
                    stack.append(a + b)
                case '-':
                    stack.append(a - b)
                case '*':
                    stack.append(a * b)
                case '/':
                    stack.append(a / b)
        else:
            stack.append(float(item))

    return stack[0]

if __name__ == '__main__':
    # Test fn
    print(npi('1 2 3 4 + * +'))