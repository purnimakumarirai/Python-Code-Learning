calculate = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} Days are {num_of_days * calculate} {name_of_unit}")

def scope_check(num_of_days):
    my_var="variable inside function"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)

scope_check(20)
