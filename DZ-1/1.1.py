#coding: utf-8

# Задание 1:

import os

lst2=[]

lst = [f for f in os.listdir('.') if not f.startswith('.')] # убираем все скрытые файлы

for i in lst:  
	
	f = open(i) 
	data = f.read()  
	a=int((data.count('python'))) 
	z=[i,a]
	print (z) #вывод результата на экран

	lst2.append(z) # для записи результата в файл
	result_file = open('result.txt', 'w')
	result_file.write(str(lst2))
	result_file.close()
