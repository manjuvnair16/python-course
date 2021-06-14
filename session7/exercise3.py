import csv
'''
3a. First, let's read our CSV file and print out each row. Copy the code below and fill in the
blanks.
'''
'''
with open('scoreboard.csv', 'r') as file:
    csvreader = csv.reader(file)
    for  row in csvreader:
        print(row)

'''
'''
3b. Now, amend your work so that the name and score for each row are printed in the
following format instead:
Misty has a high score of 4
Hint: each row is returned in a list format. How do you access each value of the list by its
index?
'''

with open('scoreboard.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0] != "name":
            print(f"{row[0].capitalize()} has a high score of {row[1]}")


'''
3c. Finally, let's add an extra row to our scoreboard. Using the append mode, underneath the
code you have already written, add a score of 2 for Brock
Hint: to get the csv writer object, you can use the .writer() method from the csv module
You can then use the .writerow() method on the csv writer object which takes a list of
your row values as input
Extension: can you add multiple rows to the csv file at once?
Hint: use the .writerows() method
'''
'''
#writing single row
with open('scoreboard.csv','a') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Brock',2])
'''


#writing multiple rows at once
with open('scoreboard.csv','a') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows([['Lisa',5],['Kudrow',8],['Amy',9],['Sheldon',10]])
    




