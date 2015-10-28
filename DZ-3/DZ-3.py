import pickle
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
			break

		elif wtd=="Вывести":
			if os.path.exists(flnm):
				q = open(flnm, 'rb')
				allcars = pickle.load(q)
				
				allcars_s_c=sorted(allcars) # сортировка по модели


				allcars_s_p=sorted(allcars, key=lambda car_n:car_n[1]) # сортировка по мощности
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


#2 Сортировка своим методом:
	
