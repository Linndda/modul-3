number = int(input('Введите число: '))
number_next = number + 1 if number >= 0 else number - 1
number_prev = number - 1 if number >= 0 else number + 1
 
print("После числа", number, "идет число", number_next, end=".\n")
print("До числа", number, "идет число", number_prev, end=".\n")