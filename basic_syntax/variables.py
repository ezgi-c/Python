# built-in type() function prints the variable type

int_value = 4
print(int_value)
print(type(int_value))  # prints <class 'int'>

print()

# built-in float() function stores the variable as type float
float_value = float(int_value)
print(float_value)  # prints 4.0
print(type(float_value))  # prints <class 'float'>

temperature = int(101.2)
print(type(temperature))

temperature = float(101.2)
print(type(temperature))

temperature = bool(101.2)  # stores temperature as type boolean
print(type(temperature))
print(temperature)  # prints True

temperature = str(101.2)
print(type(temperature))

