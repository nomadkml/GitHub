import db, main
import pickle, sys, os

# функция сохранения в cars.pickle:
def pickle_safe(allcars,flnm): 

	f=open(flnm, 'wb')
	pickle.dump(allcars,f)
	f.close()

# общая функция проверки правильности данных, введенных пользователем
def proverka(func):  
	ToF,var=func()
	while ToF is not True:
		print ('Ошибка, попробуйте еще раз')
		ToF,var=func()
	else:
		return var

# функция вывода
def vivseti(flnm): 
	if len(main.keys_list) == 0:
		print ('В базе нет ни одной записи')

	else:
		print ('Все данные:')
		for i in main.allcars:
			value = main.allcars[i]
			print (i, '-', value)

		print ('Данные, сортированные по имени:')
		for i in sorted(main.allcars):
			value = main.allcars[i]
			print (i, '-', value)
		
		sorted_list = [(k,v) for v,k in sorted([(v,k) for k,v in main.allcars.items()])]
		print ('Данные, сортированные по мощности:')
		for i in sorted_list:
			print(i)
		sys.exit(0)
		
# запускающая функция
def cycle(): 
	while True:
		wtd_inp=db.in_out('Ввести или вывести?')
		if wtd_inp == 'Ввести' or wtd_inp == 'ввести':
			data = {proverka(db.alpha):proverka(db.digit)}
			return True, data
			break
		elif wtd_inp == 'Вывести' or wtd_inp == 'вывести':
			vivseti(main.flnm)
		else:
			return None, None

# функция поиска по названию
def search_name(keys_list):
	if len(main.keys_list) == 0:
		print ('В базе нет ни одной записи')

	else:
		car_search = db.in_out ('Введите модель автомобиля или слово для поиска: ')
		for i in range(len(main.keys_list)):
			if car_search in main.keys_list[i]:
				print (main.keys_list[i], '-', main.values_list[i])
				sys.exit(0)

#функция поиска по мощности:
def search_power(values_list):
	if len(main.values_list) == 0:
		print ('В базе нет ни одной записи')

	else:
		while True:
			P1=input('Введите первое значение из промежутка: ')
			P2=input('Введите второе значение из промежутка (большее): ')

			if P1.isdigit()==True and P2.isdigit()==True:

				print ('Модели автомобилей с мощностью больше, чем', P1,':')
				for i in range(len(values_list)):
					if int(P1)<int(values_list[i]):
						print (main.keys_list[i], '-', main.values_list[i])


				print ('Модели автомобилей с мощностью меньше, чем', P1,':')
				for i in range(len(values_list)):
					if int(P1)>int(values_list[i]):
						print (main.keys_list[i], '-', main.values_list[i])

				print ('Модели автомобилей с мощностью в промежутке между', P1,'и', P2)
				for i in range(len(values_list)):
					if int(P1) < int(values_list[i]) < int(P2):
						print (main.keys_list[i], '-', main.values_list[i])
				sys.exit(0)

			else:
				print ('Должны быть только цифры')	

# общая функция поиска
def s_earch():
	while True:
		wtd1=db.in_out('Внимание! Регистр учитывается!\nПоиск по мощности (введите P) или по марке(введите М)? ')
		if (wtd1 == 'P' or wtd1 == 'Р' or wtd1 == 'M' or wtd1 == 'М')==True:
			if wtd1 == 'P' or wtd1 == 'Р':
				search_power(main.values_list)
				break
			elif wtd1 == 'M' or wtd1 == 'М':
				search_name(main.keys_list)
				break
			else:
				print ('Ошибка, попробуйте еще раз')