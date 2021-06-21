'''
******************************************
2a. To use the pokeapi (https://pokeapi.co/) to look up the pokemon called charmander
and print out the reponse, copy the code below and fill in the blanks.
Example API endpoint: "https://pokeapi.co/api/v2/pokemon/ditto"
******************************************
'''

import requests
import pprint
response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
pokemon_stats = response.json()
#pprint.pprint(pokemon_stats)


'''
******************************************
2b. Print out charmander's weight.
Hint: Can you remember how to access a dictionary value from a key?
******************************************
'''
print(f"Charmander: weight - {pokemon_stats['weight']}")


'''
******************************************
Each pokemon has some abilities.
2c. Count how many abilities charmander has and print it out.
******************************************
'''
print(f"Charmander: no. of abilities - {len(pokemon_stats['abilities'])}")
print(f"Charmander: abilities: ")
for ability in pokemon_stats['abilities']:
    print(f"- {ability['ability']['name']}")


'''
******************************************
2d. Create a list of the names of charmander's abilities.
******************************************
'''
charmander_abilities = []
for ability in pokemon_stats['abilities']:
    charmander_abilities.append(ability['ability']['name'])
print(f"{charmander_abilities}")