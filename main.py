import random

# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.

list1 = [random.randint(-10, 10) for i in range(10)]
list2 = [random.randint(-10, 10) for i in range(10)]
print(list1,'\n',list2)
task1 = list1 + list2
task2 = list(set(task1))
task3 = []
for i in list1:
  if i in list2:
    task3.append(i)
task4 = list(set(list1).difference(set(list2))) + list(set(list2).difference(set(list1)))
task5 = [min(list1), max(list1), min(list2), max(list2)]
print('1) ',task1,'\n','2) ',task2,'\n','3) ',task3,'\n','4) ',task4,'\n','5) ',task5 )