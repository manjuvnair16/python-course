'''
1a. To read and print out the contents of the file groceries.txt , copy the code below and
fill in the blanks.
'''
'''
with open('groceries.txt', 'r') as file:
    file_contents = file.read()
    print(file_contents)
    
'''


'''
1b. Next, read the contents of the file groceries.txt again but this time, only print out
the very first line from the file.
'''
'''
with open('groceries.txt','r') as file:
    print(file.readline())
'''


'''
1c. Now, use the file.readlines() method to return a list and print each item out one
by one, with the first letter of each word in the list capitalised.
Extension: print each item out with a number at the front, e.g. 1. Milk
'''
with open('groceries.txt','r') as file:
    i = 1
    for line in file.readlines():
        print(f"{i}. {line.capitalize()}")
        i = i + 1


