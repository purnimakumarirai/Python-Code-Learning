calculate = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    

    if num_of_days > 0:
        return f"{num_of_days} Days are {num_of_days * calculate} {name_of_unit}"
    elif num_of_days ==0:
        return "entered a 0"
    else:
        return "wrong value"

user_input = input("Hey user, Enter a number and will convert it into hours!\n")

user_input_num=int(user_input)

calculated_value = days_to_units(user_input_num)
print(calculated_value)


#-----------------------------------------------------------------------------------------------------------------------------------------------

calculate = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} Days are {num_of_days * calculate} {name_of_unit}"


def validate_and_execute():
    if user_input.digit():
        user_input_num = int(user_input)
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            print("you entered a 0, please enter a valid +ve number")
    else:
        print("your input is not valid number, don't ruin my code")
