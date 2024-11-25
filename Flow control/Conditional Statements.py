num = int(input('Enter a number'))
if num < 0:
    print(num,'is negative')
num = int(input('Enter another number:'))
if num > 0:
    print(num, 'is positive')
    print((num, 'is squared', num * num))
    print('bye')

# or you can just
num = int(input('Enter a number'))
if num < 0:
    print(num,'is negative')
else:
    print(num, 'is positive')
    print((num, 'is squared', num * num))
print('Bye')
