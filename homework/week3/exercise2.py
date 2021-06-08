'''
*********************************************************************************
2a. Write a dictionary named student_scores with the following key:values
Amy: 67
Billy: 70
Charlie: 90
Daisy: 75
Emily: 71

*********************************************************************************
'''
student_scores = { 
                    'Amy':     67,
                    'Billy':   70,
                    'Charlie': 90,
                    'Daisy':   75,
                    'Emily':   71,
                }
print(student_scores)



'''
*********************************************************************************
2b. Write a function named addKeyValue which takes in 2 parameters of key and value . This method should add a new key:value pair to the student_scores dictionary. 
*********************************************************************************
'''
def addKeyValue(key,val):
    student_scores[key] = val



'''
*********************************************************************************
2c. Call your method with a key of Fran and value of 85
*********************************************************************************
'''
addKeyValue('Fran', 85)
print(student_scores)



'''
*********************************************************************************
2d. Create a list named passStudents of student names who have a score of 70 or more Hint: loop through the items in the student_scores dictionary and check each score
Remove all students from the dictionary which have a score of less 70 and print the final dictionary
*********************************************************************************
'''
#Method 1 - modify the existing dictionary
#list(dict.items()) creates a new list containing refs to all key, value pairs so that the original dictionary can be modified and still be #iterable)
#print(student_scores.items(),list(student_scores.items()))  
passStudents = []
for key, value in list(student_scores.items()):    
    if value >= 70:
        passStudents.append(key)
    else:
        del student_scores[key]   
  
print(f'{passStudents = }\n{student_scores = }')


#Method 2 - create a new dictionary with the desired key, value pairs
passStudents = []
new_student_scores = {}
for key, value in student_scores.items():
    if value >= 70:
        passStudents.append(key)
        new_student_scores[key] = value
    
print(f'{passStudents = }\n{new_student_scores = }\n{student_scores = }')