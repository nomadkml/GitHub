# Задание 2:
#coding: utf-8

import math

a=45
b=338
c=19

s_lst=[]
lst = [a,b,c]

for i in lst:
	s=round((math.pi*i**2/4),2)
	s_lst.append(s)
	print('Площадь {0}-го круга'.format(lst.index(i)+1), s)

for i in range(len(s_lst)): # поиск максимального значения
	if s_lst[i]>s_lst[i-1]:
		maxim=s_lst[i]
	else:
		maxim=s_lst[i-1]

for i in s_lst: #вычитаем из большего два меньших
	if i==maxim:
		pass
	else:
		minus=maxim-i

print ('Из большей площади вычитаем меньшие - ',minus)