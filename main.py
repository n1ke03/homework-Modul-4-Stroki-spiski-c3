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
print(task1,'\n',task2)