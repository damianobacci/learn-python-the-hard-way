my_name = "Damiano Bacci"
my_age = 29
my_height = 179 # centimeters
my_weight = 69 # kilograms
my_eyes = "brown"
my_teeth = "white"
my_hair = my_eyes

print(f"Let's talk about {my_name}.")
print(f"He is {my_height} centimeters tall.")
print(f"He is {my_weight} kilograms heavy.")
print("Actually thay's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_weight} and {my_height}, I get {total}")

print("Now I will convert my weight in pounds and my height in inches.")
height_inches = my_height / 2.54
weight_pounds = my_weight * 2.205
print(f"If my height in cm is {my_height}, than my height in inches will be {round(height_inches)}.")
print(f"If my weight in kg is {my_weight}, then my weight in pounds will be {round(weight_pounds)}.")