'''
2a. To write to your first file, pokemon.txt , copy the code below and fill in the blanks.
'''

with open('pokemon.txt', 'w') as file:
    file.write("Pikachu")




'''
2b. Now we can add some more data to our file. Using the mode append instead of write this
time, underneath your block of code from 2a, add an extra pokemon name into your file such
as Charizard
Hint: the mode for append is 'a', and use \n to create a new line in the file
After running your code, check the contents of your file to see if it's correct!
'''
with open("pokemon.txt",'a') as file:
    file.write("\nCharizard")




'''
2c. Now we will try and add multiple new lines into our file at one time. Create a list of extra
Pokemon names, such as Eevee and Squirtle and use the .writelines() method
to add all your list items to the file
'''
pokemon_names = ['\nEvee','\nSquirtle','\nBulbasaur']
with open('pokemon.txt','a') as file:
    file.writelines(pokemon_names)