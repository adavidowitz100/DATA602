#Q1 Fix all the syntax and logical errors in the given source code
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the
# average is a high score. The high score variable holds the value that is considered a high score.

#needs to match the case of the variable used below
high_score = 95

# Get the test scores.
#input needs to be cast as a numerical type to do addition later
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
#There should be an input for the test3 or it should be deleted from average
test3 = float(input('Enter the score for test 2: '))
# Calculate the average test score.
#parenteses needed to maintain order of operations
average = (test1 + test2 + test3) / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
#High score should probably be sctrictly greater than but somewhat ambiguous
if average > high_score:
    print('Congratulations!')
    #This should be indented to the conditional. If you didn't get a new high score
    #the program wouldn't know if it was a good average
    print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the
#length and width of two rectangles and prints to the user the area of both rectangles.
side1 = float(input('Enter the length for rectangle 1: '))
side2 = float(input('Enter the width for rectangle 1: '))
side3 = float(input('Enter the length for rectangle 2: '))
side4 = float(input('Enter the width for rectangle 2: '))
area1 = side1 * side2
area2 = side3 * side4
print('The area for rectangle 1 is:', str(area1)+'.', 'The area for rectangle 2 is:', area2)

#Q3
#Ask a user to enter their first name and their age and assign it to the variables name and age.
#The variable name should be a string and the variable age should be an int.

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
name = input('Enter your first name: ')
age = int(input('Enter your age: '))
print("Happy birthday", name + '!', "You are", age, "years old today!")
