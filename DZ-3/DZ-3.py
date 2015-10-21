import pickle
import os
flnm = 'cars.pickle'


if os.path.exists(flnm):
	f = open(flnm, 'rb')
	allcars = pickle.load(f)

else:
	allcars=[]


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
			print (type(data))
			allcars.append(data)
			print (type(allcars))



			f=open(flnm, 'wb')
			pickle.dump(allcars,f)
			f.close()
			break

		elif wtd=="Вывести":
			if os.path.exists(flnm):
				q = open(flnm, 'rb')
				allcars = pickle.load(q)
				for i in allcars:
					print (i)
				break
			else:
				print ('База пуста. Сначала введите хотя бы одно значение')

	else:
		print ('Неверное значение, должно быть "Ввести или Вывести"')

	
	
