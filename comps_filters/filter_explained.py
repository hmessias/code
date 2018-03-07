def greater_than_3(num):
    if num > 3:
        return True
    else:
        return False

numbers = [1, 2, 3,8, 9, 10]

#Using a filter
numbers_greater_3 = list(filter(greater_than_3, numbers))

#Not using a filter
ng3 = []

for num in numbers:
    if greater_than_3(num):
        ng3.append(num)
