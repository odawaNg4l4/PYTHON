age = int(input('Please enter your age'))
print(type(age))
print(age)

exchange_rate = 1.86
print(type(exchange_rate))

int_value = 1
string_value = '1.5'
float_value = float(int_value)
print('int value as a float;', float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:', float_value)
print(type(float_value))

# Converting an input string
exchange_rate = float(input("Please enter the exchange rate to use:"))
print(exchange_rate)

# Complex numbers
c1 = 1j
c2 = 2j
print('c1:', c1, 'c2:', c2)
print(type(c1))
print(c1.real)
print(c1.imag)

