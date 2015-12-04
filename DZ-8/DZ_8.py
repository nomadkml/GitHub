#coding: utf-8

import sys
from random import randint

class farm:
	def __init__(self, ducks_number = None, cows_number = None, dogs_number = None):
		
		if ducks_number != None:
			self.ducks_number=ducks_number
		else:
			self.ducks_number = int(input ('Введите количество уток: '))

		if cows_number != None:
			self.cows_number=cows_number
		else:
			self.cows_number = int(input ('Введите количество коров: '))

		if dogs_number != None:
			self.dogs_number=dogs_number
		else:
			self.dogs_number = int(input ('Введите количество уток: '))	


	def month_pass(self,voice_n_1_lst, distance_n_1_lst, product_n_1_lst):
		animals_number = [self.ducks_number, self.cows_number, self.dogs_number]
		voice_month_lst=[]
		distance_month_lst=[]
		product_month_lst=[]
		for i,j,k,l in zip(animals_number,voice_n_1_lst,distance_n_1_lst,product_n_1_lst):
			voice_month_lst.append(i*j)
			distance_month_lst.append(i*k)
			product_month_lst.append(i*l)
		return (voice_month_lst,distance_month_lst,product_month_lst)

	def print_all(self,voice_n_1_lst, distance_n_1_lst, product_n_1_lst):
		animals = ['ducks', 'cows', 'dogs']
		products = ['eggs', 'litres of milk', 'poo']
		voice_month_lst,distance_month_lst,product_month_lst=self.month_pass(voice_n_1_lst, distance_n_1_lst, product_n_1_lst)

		for i,j,y,k,l in zip(animals,voice_month_lst, distance_month_lst, product_month_lst, products):
			print ('This month', i, 'gave voice', j, 'times, ran', y, 'metres and produced', k, l)
	
class Animal:
	
	def __init__(self,name=None, legs=4, product=None):
		
		if legs != None:
			self.legs=legs
		else:
			self.legs = int(input ('Введите количество ног: '))

		self.name = name
				
		self.product = product

	def voice(self):
		voice_number = randint (10,1000)
		return voice_number 

	def distance(self, speed=0, time=24):    # Скорость бега (км/ч) и время (мин)
		if speed == 0:
			self.speed=0
		elif speed < 0:
			print ('В каком мы измерении?')
			sys.exit(0)
		else:
			self.speed = randint((speed-randint(0,5)),(speed+randint(0,5)))

		if self.legs == 4:
			dist = self.speed*time
		elif self.legs == 2:
			dist = self.speed*time/2
		else:
			print ('Что за инвалид?')
			sys.exit(0)

		return dist

	def product_prod (self):
		product_number = randint (0,5)
		return product_number

	def month_pass (self):
		voice_month = self.voice()*30
		distance_month = self.distance(5)*30
		product_month = self.product_prod()*30
		return voice_month, distance_month, product_month

class Ducks (Animal):
	pass

class Cows (Animal):
	pass

class Dogs (Animal):
	pass


a=None
while a!='stop':
	
	Rduck=Ducks('Ducks', 2, 'eggs')

	RCow=Cows('Cows', 4, 'milk')

	RDog=Dogs('Dogs', 4, 'poo')

	voice_n_1_lst = []
	distance_n_1_lst = []
	product_n_1_lst = []

	for i,j,k in Rduck.month_pass(),RCow.month_pass(),RDog.month_pass():

		voice_n_1_lst.append(i)
		distance_n_1_lst.append(j)
		product_n_1_lst.append(k)

	farm_1 = farm(5,1,1)
	farm_1.print_all(voice_n_1_lst,distance_n_1_lst,product_n_1_lst)
	print ('Прошел месяц')
	a=input()







