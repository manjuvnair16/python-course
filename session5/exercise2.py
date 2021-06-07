'''
*********************************************************************************
2a. Create a dictionary of stats about you assigned to the variable my_stats - you could
include keys such as name , age and occupation
Try to add a new key:value pair to your dictionary
Try removing a key:value pair
Try replacing the value of one of the existing keys
Access one of the values in the dictionary and print it out
*********************************************************************************
'''
my_stats = {                     #create a dictionary of stats
            'name': 'Manju',
            'age' : 40,
            'occupation': 'HomeMaker'
           }
print(my_stats)

my_stats['location'] = 'London'  #adds a new key:value pair
print(my_stats)

del my_stats['age']              #removes a key:value pair
print(my_stats)

my_stats['occupation'] = 'Coder' #replace the value of one of the existing keys
print(my_stats)

print(my_stats.get('name'))      #access one of the values in the dictionary and print it out




'''
*********************************************************************************
2b. Now that you are a bit more familiar with the syntax, create a new dictionary called
my_pokemon with the following key:value pairs
pokemon:Rapidash
type:Fire
level:30
*********************************************************************************
'''
my_pokemon = {
                'pokemon' : 'Rapidash',
                'type'    : 'Fire',
                'level'   : 30

             }
print(my_pokemon)




'''
*********************************************************************************
2c. Your pokemon learnt a new move.
Add a new key:value pair to this dictionary with move:Flame Wheel
*********************************************************************************
'''
my_pokemon['move'] = 'Flame Wheel'
print(my_pokemon)




'''
*********************************************************************************
2d. Print out your dictionary my_pokemon
Try looping through your dictionary and printing only the values
Now try printing only the keys
Optional extension: your pokemon learnt another move. Change your move key so that the
value is a list which contains 2 moves
Flame Wheel
Agility
Print each move value one by one from the inner list using a for loop.
*********************************************************************************
'''
print(my_pokemon)                               #print your dictionary my_pokemon

for value in my_pokemon.values():               #print only the values
    print(f'Values of my_pokemon: {value}')

for key in my_pokemon.keys():                   #print only the keys  (can also use 'for key in my_pokemon:')
    print(f'Keys in my_pokemon: {key}')

my_pokemon['move'] = ['Flame Wheel','Agility']  #change your move key so that the value is a list
print(my_pokemon['move'])

for value in my_pokemon['move']:
    print(f'Moves of my_pokemon: {value}')