# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача варианта №9 Крылова 2018
Решение на языке Python 3.
Автор: Крылов, 2018
-------------------------------------------------
В лаборатории для большого количества частиц производятся замеры электрического заряда каждой из них.
Заряд частицы измеряется как целое число (положительное, отрицательное или 0).
Частиц, заряд которых измерен, может быть очень много, но не может быть меньше трёх. Заряды всех частиц различны.
В серии обязательно присутствует хотя бы одна частица с отрицательным зарядом.
При обработке результатов в каждой серии эксперимента отбирается основное множество значений зарядов.
Это такое непустое подмножество значений зарядов частиц (в него могут войти как заряд одной частицы, так и заряды всех частиц серии),
для которого произведение значений зарядов является минимальным среди всех возможных подмножеств. При нахождении произведения знак числа учитывается.
Если есть несколько таких множеств, то берётся то, которое содержит наибольшее количество элементов.
Вам предлагается написать эффективную, в том числе по используемой памяти, программу (укажите используемую версию языка программирования, например Borland Pascal 7.0),
которая будет обрабатывать результаты эксперимента, находя основное множество.
Перед текстом программы кратко опишите используемый Вами алгоритм решения задачи.На вход программе в первой строке подаётся количество частиц N.
В каждой из последующих N строк записано одно целое число, по абсолютной величине не превышающее 109. Все N чисел различны.
Пример входных данных:
4
323
0
2
-999
Пример выходных данных для приведённого выше примера входных данных:
1 3 4
"""
