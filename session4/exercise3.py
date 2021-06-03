#3. Write a function that takes 2 integers and 1 string as arguments and applies a mathematical
#operation on the integers based on the value of the string. The function should print out the
#result and not return anything.

def print_result(num1, num2, operation):
    if operation =='add':
        print(f'{num1 + num2}')

    if operation =='subtract':
        print(f'{num1 - num2}')

    if operation =='multiply':
        print(f'{num1 * num2}')

    if operation =='divide':
        print(f'{num1 / num2}')


print_result(10,4,'add')
print_result(10,4,'modulus')

    