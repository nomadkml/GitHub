import db, debug
import pickle, sys, os

# функция для ввода команды/данных 	
def in_out(text):
	inp=input('{0}: '.format(text))
	return inp

# функция ввода марки автомобиля проверки того, что она состоит только из букв латинского или русского алфавитов. Мощность только из цифр.
def alpha():  

	car=in_out('Введите марку автомобиля')
	if car.isalpha()==True:
		return True, car
	else:
		return None, None

# функция ввода можности автомобиля и проверки того, что она состоит только из цифр.
def digit(): 
	temp=in_out('Введите мощность автомобиля')
	power=int(temp)
	if temp.isdigit()==True:
		return True, power
	else:
		return None, None

def pickle_load(flnm):
	try:
		f = open(flnm, 'rb')
		allcars = pickle.load(f)
		return allcars
	except FileNotFoundError:
		print ('Файла cars.pickle пока не существет')
		allcars = {}
		return allcars
	else:
		print ('Какая-то непонятно как здесь оказавшаяся ошибка')
	finally:
		print ('Внесите первые данные для создания файла')

flnm = 'cars.pickle'
allcars = pickle_load(flnm)
values_list=[] # этот кусок кода - для фильтрации и поиска
keys_list=[]
if len(allcars) != 0:
	try:		
		for keys,values in allcars.items():
			values_list.append(values)
			keys_list.append(keys)
	except:
		print ('Что-то пошло не так')