
'''
***************************************************************************************
3. Write a function which uses a while loop to repeatedly ask the user for a number, until they terminate the program by not entering a value. The function should print the sum of each entered number.
Example output of the program:

Enter a number to add (hit enter if you don't want to add any more numbers): 4
Enter a number to add (hit enter if you don't want to add any more numbers): 16
Enter a number to add (hit enter if you don't want to add any more numbers): 3
Enter a number to add (hit enter if you don't want to add any more numbers):
Sum of numbers: 23


Hint: there are a few ways you can construct your while loop, but one option is to do while True: and then use the break statement when you want to stop running the loop

***************************************************************************************
'''

def sum_of_numbers():
   sum = 0
   while True:
       num_str = input("Enter a number to add (hit enter if you don't want to add any more numbers): ")
       if num_str == "":
           break
       sum += int(num_str)
   print(f'Sum of numbers: {sum}')

sum_of_numbers()

