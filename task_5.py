minutes = int(input('Введите количество минут: '))
# Вариант №1
clock = (minutes // 60) % 24
minute = (minutes - (minutes // 60) * 60) % 60
print(clock, minute)
 
# Вариант №2
clock = minutes // 60
minute = (minutes - (minutes // 60) * 60) % 60
print(clock, minute)