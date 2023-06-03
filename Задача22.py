# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


n = int(input("Введите количество элементов первого множества: "))
set1 = set()
for i in range(n):
    set1.add(int(input()))

m = int(input("Введите количество элементов второго множества: "))
set2 = set()
for i in range(m):
    set2.add(int(input()))

element = sorted(list(set1 & set2))
print("Общие элементы:", end=" ")
for i in element:
    print(i, end=" ")