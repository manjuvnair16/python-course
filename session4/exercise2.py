47
#2a. Write a function called shopping_calculator 

def shopping_calculator(shopping_cost,discount_applicable):
    if (shopping_cost > 20 and discount_applicable == 'y'):
        total_cost = shopping_cost * 0.9
    elif (shopping_cost >= 100 and discount_applicable == 'n'):
        total_cost = shopping_cost * 0.95
    else:
        total_cost = shopping_cost

    if (total_cost <= 30):
        total_cost = total_cost + 5
    
    return total_cost


shopping_cost = float(input('What is the total price of your shopping? '))
discount_applicable = input('Do you have a discount code? y/n ')

total_cost = shopping_calculator(shopping_cost,discount_applicable)
print(f'The total cost is {total_cost}')


#2b. Change the second argument for your function so it accepts a Boolean value instead of a string.

def shopping_calculator(shopping_cost,discount_applicable):
    if (shopping_cost > 20 and discount_applicable == True):
        total_cost = shopping_cost * 0.9
    elif (shopping_cost >= 100 and discount_applicable == False):
        total_cost = shopping_cost * 0.95
    else:
        total_cost = shopping_cost

    if (total_cost <= 30):
        total_cost = total_cost + 5
    
    return total_cost

total_cost = shopping_calculator(47, True)
print(f'The total cost is {total_cost}')
