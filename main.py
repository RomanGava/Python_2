# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


# N = int(input('Введите количество монет '))
# orel = reshka = 0
# for i in range(N):
#     x = int(input('Орел(1) или решка(0)? '))
#     if x == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel < reshka:
#     print(f'Переверните {orel} монет с орла на решку, их меньше всего')
# elif orel == reshka:
#     print(f'Количество орлов и решек одинаково, по {reshka} штук, переверните какие Вам нравятся')
# else:
#     print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# x = int(input("Петя задумал первое натуральное число X (1..1000): "))
# y = int(input("Петя задумал второе натуральное число Y (1..1000): "))
# if x < 1 or x > 1000 or y < 1 or y > 1000:
#   print('Вы ввели число не из заданного диапазона!')
# else:
#     S = x + y
#     P = x * y
#     stop = 0
#     for i in range(1001):
#         if stop != 1:
#             for j in range(1001):
#                 if stop != 1:
#                     if i * j == P and i + j == S:
#                         print(i, j)
#                         stop = 1
#             else:
#                 j = 1001
#         else:
#             i = 1001
#   Вариант 2

# x = int(input("Петя задумал первое натуральное число X (1..1000): "))
# y = int(input("Петя задумал второе натуральное число Y (1..1000): "))
# s = x + y
# p = x * y
# x1 = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
# y1 = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
# print(x1, y1)

# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Введите число N: "))
# p = 1
# while p <= n:
#     print(p, end = ', ')
#     p = p*2
# Узел связанного списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Функция для печати заданного связанного списка
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
 
 
# Переворачивает данный связанный список, изменяя его поля `.next` и
# 1ТП4Т его голова.
def reverse(head):
 
    previous = None
    current = head
 
    # пройтись по списку
    while current:
 
        # хитрый: обратите внимание на следующий узел
        next = current.next
 
        current.next = previous        # исправить текущий узел
 
        previous = current
        current = next
 
    # зафиксируйте головку так, чтобы она указывала на новый фронт
    return previous
 
 
if __name__ == '__main__':
 
    head = None
    for i in reversed(range(6)):
        head = Node(i + 1, head)
 
    head = reverse(head)
    printList(head)