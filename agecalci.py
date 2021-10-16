#Age calculator

#import datetime module
from datetime import datetime

print("A simple program to calculate your age")
print()

#present date from datetime module

date = datetime.now()
year = int(date.year)
month = int(date.month)
day = int(date.day)

#reading born year
input_year = int(input("Enter the year you were born:  "))
if input_year <= 0 or input_year > 2020:
    print("enter valid year ")
    exit()
    
#reading born month
input_month = int(input("Enter the month you were born: "))
if input_month <= 0 or input_month > 12:
    print("enter a valid month")
    exit()
    
#reading born day
input_day = int(input("Enter the day you were born: "))
if input_day <= 0 or input_day > 31:
    print("enter a valid day")
    exit()
#calculating age
    
#number of years
age_year = year - input_year

#number of months
age_month =( month - input_month)

if age_month < 0:
    age_year = age_year - 1
    age_month =( 12 - (input_month - month))
    
#number of days
age_day = day - input_day
if age_day < 0:
    age_month = age_month - 1
    age_day = 31 - (input_day - day)
    
#printing age 
print("you are " + str(age_year) + " years, " + str(age_month) + " months and " + str(age_day) + " days old.")


