'''
***************************************************************************************
1a. Write a program that prints all the numbers from 0 to 10 except multiples of 3
 
***************************************************************************************
'''
#Method 1:
for num in range(11):
    if (num % 3 != 0):
        print(num)

#Method 2 using 'continue'
for num in range(11):
    if (num % 3 == 0):
        continue
    print(num)

'''
***************************************************************************************
1b. Adjust your code so that it is written as a function called print_nums
 
***************************************************************************************
'''
def print_nums():
    for num in range(11):
        if (num % 3 != 0):
            print(num)

print_nums()

'''
****************************************************************************************************************
1c. Adjust your function so that you can input the maximum number to print upto, rather than being fixed at 10
 
****************************************************************************************************************
'''

def print_nums(num):
    for val in range(num +1):
        if (val % 3 != 0):
            print(val)

print_nums(23)