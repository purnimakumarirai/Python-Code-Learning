calculate = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} Days are {num_of_days * calculate} {name_of_unit}"

my_var = days_to_units(40)
print(my_var)
