def factorial(num):
    call_stack = []
    if num == 1:  # base case 
        print('base case reached! num is 1.')
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack: ', call_stack)
        return num * factorial(num-1)   # recursive step
    
factorial(5)