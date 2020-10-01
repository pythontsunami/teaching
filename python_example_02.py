input_number = input('What is your favorite number')


# check if input_number contains a dot, if so convert string to float
if input_number.find('.') != -1:
	input_number = float(input_number)
	print('number is a float')

# check if input_number contains a conmma, if so, replace it 
#   with a dot and convert string to float
elif input_number.find(',') != -1:
	input_number = input_number.replace(',', '.')
	input_number = float(input_number)
	print('number was separated by a comma')

# otherwise it must be an integer (not dots and no commas)
else:
	input_number = int(input_number)
	print('number is an integer')


math_res = 2 * 3 + input_number
print(math_res)

print("The result of 2 * 3 + input_number is " + str(math_res)) # here you need to convert math to string because you cannot sum a string and an integer
print("The result of 2 * 3 + input_number is {}".format(math_res)) # here you don't need to convert math to string because you are using the format method which takes care of it
print(f"The result of 2 * 3 + input_number is {math_res}") # same as the one before, except it's a different sort of method


# Logical operators 

# == , check if two objects are equal
# >, >=, check if one object is greater or greater or equal than a second object
# <, <=, check if one object is less or less or equal than a second object
# !=, check if two objects are different
