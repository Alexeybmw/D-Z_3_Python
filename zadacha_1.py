# Задайте список чисел.Напишите программу,которая найдет сумму эллементов списка,стоящих на нечетной позиции.

num_list = [2, 3, 5, 9, 3]
odd_sum = 0
odd_index_list = []
for i in range(0, len(num_list)):
      if not i % 2 == 0:
            odd_index_list.append(num_list[i])
            odd_sum += num_list[i]
print(f'На нечетных позициях:{odd_index_list}, сумма = {odd_sum}')