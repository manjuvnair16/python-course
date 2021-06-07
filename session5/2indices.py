pokemon = ['pikachu','squirtle']

print(pokemon[1])

pokemon[1] ='charizard'
print(pokemon)

pokemon.insert(0,'squirtle')
print(pokemon)

pokemon.append('snorlax')
print(pokemon)

pokemon = pokemon + ['name1','name2']
print(pokemon)

pokemon = pokemon * 2
print(pokemon)

pokemon.pop(1)
print(pokemon)

pokemon.pop()
print(pokemon)

pokemon.remove('name1')
print(pokemon)
