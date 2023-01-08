calculate = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} Days are {num_of_days * calculate} {name_of_unit}"


def validate_and_execute():
    try:

        user_input_num = int(user_input)
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            print("you entered a 0, please enter a valid +ve number")
    except ValueError:
        print("your input is not valid number, don't ruin my code")

while True:
    user_input = input("hey user, enter a number of days you want to convert it to hour")
    validate_and_execute()
