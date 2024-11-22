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

# Bools
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))

# Strings to bools
status = bool(input('Ok to proceed:'))
print(status)

home = 10
away = 15
print(home + away)
print(type(home + away))

goals_for = 10
goals_against = 5
print(goals_for - goals_against)

# Division
print('Modulus division 4 % 2:', 4%2)
print('Modulus division 3 % 2:', 3%2)

# Power
x = 4
y = 6
print(x ** y)

# None
winner = None
print('Winner is None:', winner)
print('Winner is None:', winner is None)
print(type(winner))
print('Set winner to True')
winner = True
print('Winner:', winner)
print('Winner is None:', winner is None)
print('Winner is not None:', winner is not None)
print(type(winner))



