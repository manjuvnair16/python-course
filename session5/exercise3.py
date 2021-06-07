'''
*********************************************************************************
3a. Create an empty dictionary in the file
*********************************************************************************
'''
my_pokemon = {}
print(my_pokemon)



'''
*********************************************************************************
3b. Add the following new key:value pairs to your dictionary
pokemon:Bulbasaur
type:Grass
level:5
*********************************************************************************
'''
my_pokemon = {
                'pokemon' : 'Bulbasaur',
                'type'    : 'Grass',
                'level'   :  5

             }
print(my_pokemon)




'''
*********************************************************************************
3c. Add another key:value pair with the following:
key: - moves
value - a list of "vine whip, razor leaf, growl, cut"
*********************************************************************************
'''
my_pokemon['moves'] = ['vine whip', 'razor leaf', 'growl', 'cut']
print(my_pokemon)




'''
*********************************************************************************
3d. Your Bulbasuar leveled up 5 times - update your level value to 10
*********************************************************************************
'''
my_pokemon['level'] = 10
print(my_pokemon)



'''
*********************************************************************************
3e. You want to tell Bulbasaur to use the move cut . Loop through the moves list and print
Cut move exists if the cut move exists in the list.
*********************************************************************************
'''
if 'cut' in my_pokemon['moves']:
    print('Cut move exists')

