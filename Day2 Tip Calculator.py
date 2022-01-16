#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# My Solution:

# Greeting
print("Welcome to the Tip Calculator.")
# get the total bill from the user
total_bill=input("What was the total bill? $")
# get the tip percentage
percentage_tip= int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# get the number of people
num_people = input("How many people to split the bill? ")
# calculate what each person has to pay
to_pay=(float(total_bill)/int(num_people))*(1+percentage_tip/100)
# Message to display with results
message= f"Each person should pay: ${round(to_pay,2)}"
print(message)