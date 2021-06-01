#3a. Fill in the blanks for this program which finds the even numbers from a given range of
#numbers using a for loop.

max_number = int(input('Up to which number do we need to check for? '))
for number in range(max_number):
    if (number % 2 == 0):
        print(number)   


#3b. Write a new for loop which prints out all the numbers between 10 and 20.
for value in range(10,21):
    print(value)



#3c. Write a new for loop which prints out numbers in increments of 5 between 50 and 100,
#but skips the number 75.

for val in range(50,100,5):
    if (val == 75):
        continue
    print(val)