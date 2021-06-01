#2a. Now that you've finished your online shopping program, you want to pay for your shirt.
#Let's fill in the blank for a program to calculate the total cost and apply a discount if
#applicable.

#shopping_cost = float(input('What is the total price of your shopping? '))
#discount_applicable = input('Do you have a discount code? y/n ')
#if (shopping_cost > 20 and discount_applicable == 'y'):
#   total_cost = shopping_cost * 0.9
#else:
#    total_cost = shopping_cost

#print(f'The total cost is {total_cost}')


#2b. Customers that spend £100 or more (that don't have a discount code) automatically get
#a 5% discount. And an elif statement to your program, in between the if and else
#statements, to check for this and apply the discount.

#Shipping is £5, but orders over £30 (after discounts have been applied)
#get free shipping. Any applicable discounts do not apply to shipping.

shopping_cost = float(input('What is the total price of your shopping? '))
discount_applicable = input('Do you have a discount code? y/n ')
if (shopping_cost > 20 and discount_applicable == 'y'):
    total_cost = shopping_cost * 0.9
elif (shopping_cost >= 100 and discount_applicable == 'n'):
    total_cost = shopping_cost * 0.95
else:
    total_cost = shopping_cost

if (total_cost <= 30):
    total_cost = total_cost + 5

print(f'The total cost is {total_cost}')