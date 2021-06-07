'''
***************************************************************************************
2. Create a function with an empty body called letter_count, which takes two parameters as input - word and letter
The function should return the number of times that the inputted letter appears in the inputted word
It should be case insensitive, so that it does not matter if the input is lowercase or uppercase Test your function with the following inputs to check that it works:
word = "Bananas" letter = "n"
Output: 2

word = "Tarantula" letter = "t"
Output: 2

***************************************************************************************
'''

#Method 1
def letter_count(word, letter):
    return word.lower().count(letter.lower())

print(letter_count("Tarantula", "A"))

'''
#Method 2
def letter_count(word, letter):
    count = 0
    for each_letter in word:
        if each_letter.lower() == letter.lower():
            count += 1
    return count

print(letter_count("Banana", "A"))
'''