#This assignment was completed collaboratevly with group 1

#Q1
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[:])
print(numbers[:5])

#Q2
days = ["Sunday", "Monday","Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
sales = []
total_sales = 0
for day in days:
  amount = float(input("Enter the sales for " + day + ": "))
  sales.append(amount)
  total_sales += amount
print("The total sales for the week was",total_sales)

#Q3:
lst_places = ['Berlin', 'Nairobi', 'Tokyo', 'Stockholm', 'Moscow']
print(lst_places)
lst_places.sort()
print(lst_places)
lst_places.sort(reverse = True)
print(lst_places)

#Q4:
my_dict = {
  "602": {
    "room_number": "1",
    "instructor_name": "Prof_S",
    "meeting-time": "Thursday"
  },
  "605": {
    "room_number": "2",
    "instructor_name": "Prof_A",
    "meeting-time": "Friday"
  }
}
input_1 = input("Please enter a course number: ")

print(my_dict[input_1])

#Q5
email_dic = {"Larry": "larry@gmail.com", "Barry": "barry@gmail.com"} # Create Dictionary
print(email_dic)
#lookup email
print(email_dic["Barry"])
#add a new name/email
email_dic["Mike"] = "mike@gmail.com"
print(email_dic)
# update existing email
email_dic["Larry"] = "larry@yahoo.com"
print(email_dic)
# delete an existing name and email address
del email_dic["Mike"]
print(email_dic)
