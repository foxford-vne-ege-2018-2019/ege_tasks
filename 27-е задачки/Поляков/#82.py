# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-82.
Решение на языке Python 3.
 Автор: А. Жуков, 2018
-------------------------------------------------
82) (А. Жуков) В вход программы поступают N <= 1000 натуральных чисел,
каждое из которых не превышает 10000. Необходимо определить количество пар
элементов (ai, aj) этого набора, в которых 1 <= i < j  <= N, сумма элементов
нечётна, произведение делится на 13, , а номера чисел в последовательности
отличаются менее, чем на 5. Напишите эффективную по времени и
по памяти программу для решения этой задачи.

Описание входных и выходных данных:
В первой строке входных данных задаётся количество чисел N (1 ≤ N ≤ 1000).
В каждой из последующих N строк записано одно натуральное число, не
превышающее 10000.
Пример входных данных:
7
4
14
27
33
7
2
13
Пример выходных данных для приведённого выше примера входных данных:
1
В приведённом наборе из 7 чисел имеется одна пара (2, 13), сумма
элементов которой нечётна, произведение кратно 13, и номера
элементов в паре отличаются менее, чем на 5.
"""
N = int(input())
for i in range(N):
    x = int(input())
    if x%13 == 0:

