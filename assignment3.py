#1 Write a program that prompts the user for a meal: breakfast, lunch, or dinner.
#Then using if statements and else statements print the user a message recommending a meal.
#For example, if the meal was breakfast, you could say something like, “How about some bacon
#and eggs?” The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.

def meal_suggestions():
    vec_meal = str(input("Type your meal ")).lower()
    if vec_meal not in ['breakfast', 'lunch', 'dinner']:
        print("Please input breakfast, lunch, or dinner")
    elif vec_meal == 'breakfast':
        print('How about some bacon and eggs?')
    elif vec_meal == 'lunch':
        print('How about salad?')
    elif vec_meal == 'dinner':
        print('How about ramen?')

meal_suggestions()

# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s
#gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays
#them 1.5 times their regular hourly pay rate for all hours over 20.
# You should take in the user’s input for the number of hours worked, and their rate of pay.

def gross_pay(hours, rate):
  total_pay = 0
  if hours > 20:
    total_pay += 20 * rate
    total_pay += (hours - 20) * 1.5 * rate
  else:
     total_pay += hours * rate
  return total_pay

hours = float(input("How many hours did you work this week? "))
rate = float(input("What is your hourly pay rate? "))
print(gross_pay(hours, rate))

# #Q3: Write a function named times_ten. The function should accept an argument and
#display the product of its argument multiplied times 10.

def times_ten (x) :
  return(x*10)

print(times_ten(float(input ("enter a number "))))

# Q4: Find the errors, debug the program, and then execute to show the output.

def main(): # Add colon
      calories1 = float(input( "How many calories are in the first food?")) # rename lowecase, set as float type
      calories2 = float(input( "How many calories are in the first food?")) #rename lowecase, set as float type
      showCalories(calories1, calories2)

def showCalories(calories1, calories2): # Add colon
   print(f"The total calories you ate today {calories1 + calories2}") # use f string


# # Q5: Write a program that uses any loop (while or for) that calculates the total
#of the following series of numbers: 1/30 + 2/29 + 3/28 ............. + 30/1

list_x = []
for i in range(1, 31):
  x = (i)/(31-i)
  list_x.append(x)

sum(list_x)

#Q6: Write a function that computes the area of a triangle given its base and height.
#The formula for an area of a triangle is:AREA = 1/2 * BASE * HEIGHTFor example, if the base
# was 5 and the height was 4, the area would be 10.triangle_area(5, 4)   # should print 10

def triangle(base, height):
  """
  Takes in base height computes area of tri
  """
  area = (base * height)/2
  return(area)

base = float(input("Enter base: "))
height = float(input("Enter height: "))
answer = triangle(base,height)
print(f"The area of your triangle is {answer}")
