import pickle
import os
flnm = 'cars.pickle'

if os.path.exists(flnm):
	f = open(flnm, 'rb')
	allcars = pickle.load(f)

else:

	allcars=[]


wtd=input('Ввести или Вывести? ')

def get_smthng(what, proverka):
	while True:
		car = input('Введите {} автомобиля: '.format(what))
		if proverka(car)==True:
			return car			
		else:
			print ('Марка автомобиля может содержать только буквы')

if wtd=='Ввести':
	car = get_smthng('марку', lambda car: car.isalpha())
	car = get_smthng('мощность', lambda car: car.isdigit())

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
	data={
	car:power
	}
	allcars.append(data)
	f=open(flnm, 'wb')
	pickle.dump(allcars,f)
	f.close()

	print (allcars)
elif wtd=="Вывести":
	if os.path.exists(flnm):
		q = open(flnm, 'rb')
		allcars = pickle.load(q)
		print 

	else:
		print ('Сначала введите хотя бы одно значение')

else:
	print (Печаль)

	
	
