'''
************************************************
3a. Create variable for the following values, the name of the variable should be its type followed by underscore and var:
e.g: False => boolean_var = False
     8.98, 4, 'Jam'
************************************************
'''

float_var = 8.98
int_var = 4
string_var = 'Jam'


'''
************************************************
3b. Call a method on each of the variables you've created, print out its value using f-strings and underneath write a comment explaining what it does
hint: dir method
************************************************
'''

print(dir(float_var))
print(float_var.__sizeof__())
# __sizeof__() returns the size of the object without any garbage collector overhead.

print(dir(int_var))
print(int_var.as_integer_ratio())
# as_integer_ratio() returns a pair of integers whose ratio is equal to the original integer/float value and with a positive denominator

print(dir(string_var))
print(string_var.__contains__('a'))
# __contains__() returns true if the given string is part of the original string, else returns False

 