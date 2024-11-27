# # # while
# # count = 0
# # print('Starting')
# # while count < 10:
# #     print(count, '', end = '')
# #     count += 1
# # print()
# # print('Done')
# #
# # # for
# # print('Print out values in a range')
# # for i in range(0, 10):
# #     print(i, '', end='')
# # print()
# # print('Done')
# #
# # # incremented by 2
# # print('Print out values in a range')
# # for i in range(0, 10, 2):
# #     print(i, '', end='')
# # print()
# # print('Done')
# #
# # # Anonymous loop variable
# # for _ in range(0, 10):
# #     print('.', end='')
# # print()
#
# # Break loop statement
# print('Only print code if all iterations completed')
# num = int(input('Enter a number to check for:'))
# for i in range(0, 6):
#     if i ==num:
#         break
#     print(i, '', end='')
# print('Done')

# Continue loop
for i in range(0, 10):
    print(i, '', end='')
    if i % 2  == 1:
        continue
    print('Hey its an even number')
    print('We love even numbers')
print('Done')
