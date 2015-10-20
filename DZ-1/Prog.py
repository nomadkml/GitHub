#coding: utf-8
import os
lst2=[]
lst3=[]
lst = os.listdir('.') # запись в переменную lst списка файлов из папки, в которой находится программа
for i in lst: # цикл, который проходит по всем элементам (файлам) в папке, начиная с 0
	print(i) # выводит название файлов по порядку
	lst2.append(i)
	i1=lst2
	f = open(i) # открывает файлы
	data = f.read()  # записывает в переменную data данные из f, т.е. текст из файлов 
	a=str((data.count('python'))) # выводит количество слов "python" в каждом из файлов
	print (a)
	lst3.append(a)
	i2=lst3
	y=i1,i2
	z=str(y)
	result_file = open('result.txt', 'w')
	result_file.write(z)
	result_file.close()
