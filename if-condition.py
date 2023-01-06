calculate = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    condition_check = num_of_days >0
    print(type(condition_check))
    if num_of_days > 0:
        return f"{num_of_days} Days are {num_of_days * calculate} {name_of_unit}"
    else:
        return "wrong value"

user_input = input("Hey user, Enter a number and will convert it into hours!\n")

user_input_num=int(user_input)

calculated_value = days_to_units(user_input_num)
print(calculated_value)
