#coding: utf-8
import os
lst = os.listdir('.') # запись в переменную lst списка файлов из папки, в которой находится программа
lst2 = []
lst3 = []
l=0
for i in lst: # цикл, который проходит по всем элементам (файлам) в папке, начиная с 0
	lst2.append(i)
	f = open(i) # открывает файлы
	data = f.read()  # записывает в переменную data данные из f, т.е. текст из файлов 
	a = str(data.count('python')) # выводит количество слов "python" в каждом из файлов
	lst3.append(a)
	l1=lst2[l]
	l2=lst3[l]
	l3=l1,l2
	l4=str(l3)
	l=l+1
	print (l4)
	l5=print (l4)
	print (l5)
	file = open('result.txt', 'w')
	file.write(l4)
	file.close()