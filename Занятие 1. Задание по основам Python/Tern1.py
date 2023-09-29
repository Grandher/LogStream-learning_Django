numbers = [1, 2, 3, 4, 5, 6, 237, 238, 240, 242]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 0:
        print(number, end=" ")
