num = int(input('Enter a number'))
if num < 0:
    print(num,'is negative')
num = int(input('Enter another number:'))
if num > 0:
    print(num, 'is positive')
    print((num, 'is squared', num * num))
    print('bye')

# or you can just else
num = int(input('Enter a number'))
if num < 0:
    print(num,'is negative')
else:
    print(num, 'is positive')
    print((num, 'is squared', num * num))
print('Bye')

# elif
savings = float(input('Enter how much you have in savings:'))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print("A litu bit of money")
elif savings < 1000:
    print("Promising amount")
elif savings < 10000:
    print("Welcome aboard maam")
else:
    print("Thank you!")

