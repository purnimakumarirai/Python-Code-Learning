import datetime

user_input = input("Enter your goal with a deadline separeted with colon\n")
#input function for user input

input_list = user_input.split(":")
#split for spliting the user input wiht colon ':'

goal = input_list[0]
#variable goal 1st value in list

deadline = input_list[1]
#variable deadline 2nd value in list

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
#deadline date time 

today_date = datetime.datetime.today()
#todays date

time_till = deadline_date - today_date
#calculate how many days from now till deadline


print(f"User! TIME RemaNining for your goal:{goal} is {time_till.days}")
#printing the user to remind the goal.
