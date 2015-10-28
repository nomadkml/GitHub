# Задание 3:
#coding: utf-8

a = [1, -20, 38, 0, 44]
b = [88, -20, 48, 4, 33, 2]

#1 поиск наименьшего элемента по спискам

if len(a)<=len(b):  # проверка на количество элементов в списке.
	key=len(a)
else:
	key=len(b)

lst = [] # сравнение элементов

for i in range(key):
	if b[i]>a[i]:
		k=a[i]
	elif b[i]==a[i]:
		k='equal'  # если значения одинаковы
	else:
		k=b[i]
	lst.append(k)
	
print(lst)

#2 Сравнение модулей

for i in range(key):
	absm = abs(a[i]-b[i])
	if absm<15:
		print (i+1,':',absm,'Congrats, bro')
	else:
		print (i+1,':',absm)