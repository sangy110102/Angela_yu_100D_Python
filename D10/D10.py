#calculator

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return 'invalid input'
    return a/b
    

def pow(a,b):
    return a**b

operation = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
    "**": pow
}


def calculator():
    n1 = float(input("Enter the first number :"))
        
    should_continue = True

    while should_continue:
        for symbol in operation:
            print(symbol)
        
        operation_symbol = input("Enter the opertion you wanna perform on it : ")
        
        n2 = float(input("Enter the second number : "))
        
        calculation_function = operation[operation_symbol]
        
        result = calculation_function(n1,n2)
        
        print(f'{n1} {operation_symbol} {n2} = {result}')
        
        keep_continuing = input("Do you wanna continue with the calculated result (y) or start a new calculation (n)? ")
        
        if(keep_continuing == 'y'):
            n1 = result
        else:
            should_continue = False
            #calculator()

should_continue = True

while should_continue:
    print("Calculator")
    calculator()
    keep_continuing = input("Do you wanna exit the calculator?(y) ")
    if keep_continuing == 'y':
        should_continue = False
    else:
        calculator()
    
