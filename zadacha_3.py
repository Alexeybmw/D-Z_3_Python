# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


import random


num_n = int(input("Введите длинну списка: "))
list_numbers = []
new_n = 0 
for i in range(num_n):
      new_n = round(random.uniform(0.00, 10.00), 2)
      list_numbers.append(new_n)
print(list_numbers)
max_num = round(list_numbers[0] % 1, 2)
min_num = round(list_numbers[0] % 1, 2)
list2 = [num % 1 for num in list_numbers if num % 1 > 0.1]

print(max(list2))
print(min(list2))
print(round((max(list2) - min(list2)), 2))