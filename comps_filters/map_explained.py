numbers = [1, 2, 3,8, 9, 10]

def add_10(num):
    return num + 10

# with map
numbers_plus_10 = list(map(add_10, numbers))

# without map
nump10 = []
for number in numbers:
    nump10.append(add_10(number))
