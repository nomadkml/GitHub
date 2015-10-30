import pickle, sys, site
import os
flnm = 'cars.pickle'


if os.path.exists(flnm):
	f = open(flnm, 'rb')
	allcars = pickle.load(f)
	dict_cars={}
	for i in range(len(allcars)): # это костыль. Изначально прога делалась с помощью списков. Чтобы всё заново не переделывать, для фильтрации/поискаделаем словарь здесь.
		dict_cars.update({allcars[i][0]:allcars[i][1]})

else:
	allcars=[]


#1 Ввод и вывод марки и мощности автомобиля:

while True:
	wtd=input('Ввести или Вывести? ')
	if (wtd == 'Ввести' or wtd == 'Вывести')==True:

		if wtd=='Ввести':
			while True:
				car=input('Введите марку автомобиля: ')
				if car.isalpha()==True:
					break			
				else:
					print ('Марка автомобиля может содержать только буквы')

			while True:
				power=input('Введите мощность автомобиля: ')
				if power.isdigit()==True:
					break
				else:
					print ('Марка автомобиля может содержать только цифры')

			data = [car,power]
			allcars.append(data)


			f=open(flnm, 'wb')
			pickle.dump(allcars,f)
			f.close()
			exit()

		elif wtd=="Вывести":
			if os.path.exists(flnm):
				q = open(flnm, 'rb')
				allcars = pickle.load(q)
				
				allcars_s_c=sorted(allcars) # сортировка по модели


				allcars_s_p=sorted(allcars, key=lambda car_n:int(car_n[1])) # сортировка по мощности
				print ('Сортировка по модели:')
				for i in allcars_s_c:
					print (i)

				print ('Сортировка по мощности:')
				for i in allcars_s_p:
					print (i)
				break
			else:
				print ('База пуста. Сначала введите хотя бы одно значение')

	else:
		print ('Неверное значение, должно быть "Ввести или Вывести"')


#2 Фильтрация, поиск:
values_list=[]
keys_list=[]
for keys,values in dict_cars.items():
	values_list.append(values)
	keys_list.append(keys)
	
while True:
	wtd1=input('Внимание! Регистр учитывается!\nПоиск по мощности (введите P) или по марке(введите М)? ')
	if (wtd1 == 'P' or wtd1 == 'Р' or wtd1 == 'M' or wtd1 == 'М')==True:
		if wtd1 == 'P' or wtd1 == 'Р':
			while True:
				P1=input('Введите первое значение из промежутка: ')
				P2=input('Введите второе значение из промежутка (большее): ')

				if P1.isdigit()==True and P2.isdigit()==True:

					print ('Модели автомобилей с мощностью больше, чем', P1,':')
					for i in range(len(values_list)):
						if int(P1)<int(values_list[i]):
							print (keys_list[i])


					print ('Модели автомобилей с мощностью меньше, чем', P1,':')
					for j in range(len(values_list)):
						if int(P1)>int(values_list[j]):
							print (keys_list[j])

					print ('Модели автомобилей с мощностью в промежутке между', P1,'и', P2)
					for j in range(len(values_list)):
						if int(P1) < int(values_list[j]) < int(P2):
							print (keys_list[j])
					break

				else:
					print ('Должны быть только цифры')
		if wtd1 == 'M' or wtd1 == 'М':
			car_search = input ('Введите модель автомобиля или слово для поиска: ')
			for i in range(len(keys_list)):
				if car_search in keys_list[i]:
					print (keys_list[i])

		break
	else:
		print ('Попробуйте еще раз, нажмите любую клавишу')
		input()





