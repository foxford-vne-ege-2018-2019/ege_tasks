# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-90.
Решение на языке Python 3.
Автор: Дмитрий Муфаззалов, 2018
-------------------------------------------------
91) Логистическая компания перевозит грузы, упакованные в коробки одинакового размера.
При транспортировке коробки помещаются в контейнеры. В распоряжении компании
имеется N контейнеров (1≤ N ≤ 10**5). Каждый контейнер заполнен некоторым (возможно
нулевым) количеством коробок. Компания получила партию грузов, упакованных в M
 коробок (0 ≤ M ≤ 10**4). Требуется распределить новую партию грузов по контейнерам
 так, чтобы количество коробок в самом заполненном контейнере было наименьшим из
 возможных. Под самым заполненным понимается контейнер с таким количеством коробок,
 больше которого нет ни в каком другом контейнере. Предполагается, что в каждом
 контейнере имеется достаточно свободного места, чтобы вместить все коробки из новой
 партии. Напишите эффективную по времени и по памяти (или по одному из этих критериев)
 программу, определяющую наименьшее возможное количество коробок в наиболее заполненном
 контейнере.
Входные данные: в первой строке записаны числа N и M. В следующих N строках приведено
по одному целому числу ¬¬– количество коробок в каждом из N контейнеров до распределения новых грузов.
Выходные данные: в качестве ответа выведите одно число – минимально возможное
количество коробок в наиболее заполненном контейнере.
Пример входных данных:
5 20
1
2
3
4
5
Пример выходных данных для приведённого выше примера входных данных:
7
"""
N,M = map(int,input().split())
a=[]
for i in range(N):
    a.append(int(input()))
a.sort(reverse=True) #Сортируем массив по мере убывания
for i in range(1,N): #Делаем равные контейнеры
    while a[0] != a[i]:
        a[i] += 1
        M -= 1
if M%N == 0: #если число ящиков кратко контейнерам, то все ящики будут иметь одинаковый размер, т.е к большему нужно добавить кол-во оставшихся ящиков делённое на кол-во контейнеров
    print(int(a[i]+M/N))
else: #а если не кратко, то в большем(их) контейнере(ах) будет на 1 ящик больше, чем в остальных.
    print(int(a[i]+M//N+1))


