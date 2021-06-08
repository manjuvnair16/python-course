'''
*********************************************************************************
3a. Convert the string question to a list so it prints out
['q','u','e','s','t','i','o','n']
*********************************************************************************
'''
str_var = 'question'
str_list = []
for letter in str_var:
    str_list.append(letter)
print(str_list)



'''
*********************************************************************************
3b. Given a list of lists, create a function that finds and print the list with the largest sum as well as the sum itself
Example input: [[5,3,2],[1,3,2,1],[3,2,3],[10,1,5],[6,7,2]]
Output: The list with the largest sum is [10,1,5], sum = 16
Hint: you may also want to create a second function which you call for each list, which sums the items in an individual list
*********************************************************************************
'''
def sum_list(list):
    sum = 0
    for val in list:
        sum += val
    return sum

def largest_sum(nested_list):
    max_sum = 0
    for each_list in nested_list:
        sum_of_list = sum_list(each_list)
        if sum_of_list > max_sum:
            max_sum = sum_of_list
            max_list = each_list
    return max_sum, max_list


list_var = [[5,3,2],[1,3,2,1],[3,2,3],[10,1,5],[6,7,2]]
max_sum, max_list = largest_sum(list_var)
print(f'The list with the largest sum is {max_list}, sum = {max_sum}')



'''
*********************************************************************************
3c. You're at a supermarket and this is a dictionary of all the items it sells along with every item's price in pounds
item_price = { "apple" = 0.50,
"banana" = 0.10,
"mango" = 1.20,
"pasta" = 0.75,
"bread" = 1.00,
"milk" = 0.80,
"lettuce" = 0.90,
"egg" = 0.15,
"chicken" = 2.10
}
You need to buy the following things from this shopping list:
6 apples, 2 mangoes, 8 loaves of bread, 5 eggs, 2 packs of chicken

Print the following message with the total price of your groceries:
The total cost of my groceries is £X

Hint: create a dictionary with your shopping list and loop through it
*********************************************************************************
'''
item_price = {
               "apple"  : 0.50,
               "banana" : 0.10,
               "mango"  : 1.20,
               "pasta"  : 0.75,
               "bread"  : 1.00,
               "milk"   : 0.80,
               "lettuce": 0.90,
               "egg"    : 0.15,
               "chicken": 2.10
            }

shopping_list = {
                    "apple"  : 6,
                    "mango"  : 2,
                    "bread"  : 8,
                    "egg"    : 5,
                    "chicken": 2
                }

total_cost = 0
for key, value in shopping_list.items():
    total_cost += value * item_price[key]

print(f'The total cost of my groceries is £{total_cost:.2f}')




'''
*********************************************************************************
3d. Write a function which will ask the user to input how many of each item in item_price they would like, and prints out the total cost at the end in the following format:
Your shopping will cost £X

*********************************************************************************
'''

def calc_cost():
    print('Please enter the number of items you wish to buy from the menu below:')
    for key,value in item_price.items():
       shopping_list[key] = int(input(f'Item: {key}, Price: {value}:'))

    total_cost = 0
    for key, value in shopping_list.items():
        total_cost += value * item_price[key]
    
    print(f'Your shopping will cost £{total_cost:.2f}')

calc_cost()

    