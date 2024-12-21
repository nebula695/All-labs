# Задание 1:  Импорт стандартных модулей
import math , datetime
t = datetime.datetime.now()

print(f"Квадратный корень заданного числа {math.sqrt(int(input('Введите число: ')))}")
print(f"Дата и время{t}","\n")

# Задание 2: Создание и использование собственного модуля
from my_module import fun_function
print(f"Использование собственного модуля {fun_function(4,8)}","\n")

# Задание 3: Создание и использование пакетов
from my_moduls import mathematic
from my_moduls import string_operations


result_add = mathematic.add(5, 3)
result_subtract = mathematic.subtract(5, 3)

result_concat = string_operations.concat("Hello, ", "World!")
result_uppercase = string_operations.uppercase("hello")

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Concatenation:", result_concat)
print("Uppercase:", result_uppercase)