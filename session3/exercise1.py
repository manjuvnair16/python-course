#1a. You have a budget of £25 and want to buy a shirt online from Boohoo.
#Fill in the blanks to write a program which finds if a shirt 
#within £25 is available or not.

#shirt_price = float(input('What is the price of the shirt? '))
#shirt_in_budget = shirt_price <= 25.00
#print(f'Shirt is available within budget: {shirt_in_budget}')




#1b. Add code to your online shopping program to also check the colour of the shirt. You
#would like the shirt to be yellow. The output should now say whether the cost is within
#budget AND whether it is yellow.
shirt_price = float(input('What is the price of the shirt? '))
shirt_colour = input('Enter the colour of the shirt: ')
 
shirt_avail =  shirt_price <= 25.00 and shirt_colour.lower() == 'yellow'

print(f'Shirt is available within budget and correct colour: {shirt_avail}')