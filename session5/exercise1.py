'''
*********************************************************************************
1a. Create a list that contains multiple pokemon (Google pokemon list for Pokemon
names if needed!) and assign it to the variable pokemon`
Can you add items to your list?
Can you remove an item from your list using the value?
Can you remove an item from your list using the index?
Can you print the third item of your list?
*********************************************************************************
'''
pokemon = ['Charizard','Pikachu','Snorlax','Charmandar']
pokemon.append('Beautifly')
pokemon.insert(2,'Ditto')
print(pokemon)



'''
*********************************************************************************
1b. Create another list called my_team with the values below:
Landorus, Weedle, Spearow, Pidgey, Gardevoir
*********************************************************************************
'''
my_team = ['Landorus', 'Weedle', 'Spearow', 'Pidgey', 'Gardevoir']
print(my_team)



'''
*********************************************************************************
1c. Can you concatenate the lists from 1a and 1b and name it pokedex ?
*********************************************************************************
'''
pokedex = pokemon + my_team
print(pokedex)



'''
*********************************************************************************
1d. You've caught a wild Rattata - can you add it to position three of the pokedex ?
*********************************************************************************
'''
pokedex.insert(2,'Wild Rattata')
print(pokedex)



'''
*********************************************************************************
1e. You need to do an inventory of your pokedex - can you count how many pokemon you
own?
*********************************************************************************
'''
print(len(pokedex))



'''
*********************************************************************************
1f. Use a for loop to print out each value of your pokedex list one by one
*********************************************************************************
'''
for each_pokemon in pokedex:
    print(each_pokemon)



'''
*********************************************************************************
1g. Write an if statement which checks whether the value Charizard is contained in your
pokedex list, and prints out Charizard is in the pokedex
Hint: use the in keyword
*********************************************************************************
'''
if 'Charizard' in pokedex:
    print('Charizard is in the pokedex')