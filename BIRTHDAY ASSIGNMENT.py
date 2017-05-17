import calendar

#this program asks you to enter the following birthday information and it returns to you the exact day and year in which you was born

age = int(input("what is your age?:\n "))

date = int(input("what is your date Of Birth?:\n"))

month = int(input("you was born in which month:\n"))

current_year = int(input("type in the current year:\n"))

year_of_birth = current_year - age

day_of_birth = calendar.weekday(year_of_birth, month, date)

day_string = calendar.day_name[day_of_birth]

print("You were born on a " + day_string + " in " + str(year_of_birth))
