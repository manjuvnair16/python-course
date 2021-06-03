#1a. Write a function that takes a string name variable as its only argument and prints hello to
#the name passed in.

def greet_person(name):
    print(f'Hello {name}')

greet_person('Tom')
greet_person('Dick')
greet_person('Harry')


#1b. Write another function that takes a single number as an argument and returns True if
#the number is even and False if it is not. Call this function a few times with different
#inputs, assigning the return value of the function to a variable and then printing it out.

def check_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False

is_even = check_even(577)
print(f'Is the number even: {is_even}')

