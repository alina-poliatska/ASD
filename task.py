#Поиск первого вхождения методом грубой силы, приведенный в книге
#Удобен в использовании для низкоуровневих языков программирования
from random import randrange

def match(massive, element):
    i = 0
    while i < len(massive) and massive[i] != element:  #Лишняя проверка (i < len(massive) на кождом шаге итерации
        i += 1
    if i == len(massive):
        return "Massive have not this element"
    else:
        return i

#Улучшение эффективности алгортма путем прибавления искомого элемента в конец массива

def match1(massive, element):
    i = 0
    massive.append(element)   #прибавление искомого элемента в конец массива
    while massive[i] != element:
        i += 1
    if i == len(massive) - 1:
        return "Massive have not this element"
    else:
        return i
