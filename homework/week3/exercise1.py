'''
*********************************************************************************
1a. Create a new list with the following items and name the list my_list
"Amy", 1, "Beth", "Charlie", 6, "Daisy", 7, 2
*********************************************************************************
'''
my_list = ["Amy", 1, "Beth", "Charlie", 6, "Daisy", 7, 2]
print(my_list)



'''
*********************************************************************************
1b. Replace Beth with Sandy
*********************************************************************************
'''
my_list[2] = "Sandy"
print(my_list)



'''
*********************************************************************************
1c. For every number in the list, multiply it by itself (e.g. '6' should become '36' within the list)
Hint: use the type() function to check if each item is a number
*********************************************************************************
'''
#Method 1
for i in range(len(my_list)):
    if type(my_list[i]) == int or type(my_list[i]) == float:
        my_list[i] *= my_list[i]
print(my_list)

#Method 2
for item in my_list:
    if type(item) == int or type(item) == float:
        i = my_list.index(item)
        my_list[i] *= my_list[i]
print(my_list)



'''
*********************************************************************************
1d. Count the number of integers which are over 5 in the new list
*********************************************************************************
'''
count = 0
for item in my_list:
    if type(item) == int or type(item) == float:
        if item > 5:
            count += 1
        
print(my_list,count)