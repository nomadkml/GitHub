# Задание 4:
#coding: utf-8

while True: #ввод чисел и проверка, что digit
	a=input('Введите первое число: ')
	b=input('Введите второе число: ')
	first=int(a)
	second=int(b)
	if a.isdigit()==True and b.isdigit()==True:
		break
	else:
		print ('Ошибка')

while True: #ввод действия и проверка, введено верное значение
	action=input('Доступны следующие действия: + (сложение), -(вычитание), /(деление), *(умножение). Укажите нужное действие (одним символом): ')
	if action=='+' or action=='*' or action=='-' or action=='/':
		break
	else:
		print ('Ошибка')

if action == '+':
	result=first+second
elif action == '-':
	result=first-second
elif action == '*':
	result=first*second
else:
	result=first/second

print ('Результ - ',result)

