cars = 100 # the variable cars is assigned the 100 value
space_in_a_car = 4.0 # the variable space_in_a_car is assigned the 4.0 values (floating number)
drivers = 30 # the variable drivers is assigned the 30 values
passengers = 90 # the variable passengers is assigned the 90 values
cars_not_driven = cars - drivers # operation
cars_driven = drivers # we state that two variables are equal
carpool_capacity = cars_driven * space_in_a_car # operation
average_passengers_per_car = passengers / cars_driven # operation

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")