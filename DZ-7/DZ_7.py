#coding: utf-8

class Tank:
	
	def __init__(self,model):
		self.model = model
		self.shassi = True
		self.gusen = True
		self.speed = None

	def status(self):
		self.speed = int(input('Введите скорость ' + self.model + ': '))
		if self.speed == 0 and self.shassi == True and self.gusen == True:
			print (self.model, 'cтоит и готов к движению')
		elif self.shassi == False or self.gusen == False:
			print (self.model, 'стоит, так как сломан')
		elif self.speed > 0 and self.shassi == True and self.gusen == True:
			print (self.model, 'едет со скоростью', self.speed)
		else:
			print ('С', self.model, 'происходит какая-то чертовщина')


class Car:
	
	def __init__(self,model,wheels=4,speed=None):
		self.model = model
		self.wheels = wheels
		self.speed = speed

	def status(self):
		if self.speed == None:
			self.speed = int(input('Введите скорость ' + self.model + ': '))
		if self.speed == 0 and self.wheels == 4:
			print (self.model, 'cтоит и готов к движению')
		elif self.wheels < 4:
			print (self.model, 'стоит, так как сломан')
		elif self.speed > 0 and self.wheels == 4:
			print (self.model, 'едет со скоростью', self.speed)
		else:
			print ('С', self.model, 'что-то не так')

class Telega:
	
	def __init__(self,wheels=4):
		self.wheels = wheels
		self.speed = None

	def status(self):
		self.speed = int(input('Введите скорость объекта: '))
		if self.speed == 0 and self.wheels == 4:
			print ('Телега cтоит и готов к движению')
		elif self.wheels < 4:
			print (self.model, 'стоит, так как сломан')
		elif self.speed > 0 and self.wheels == 4:
			print ('Телега едет со скоростью', self.speed)
		else:
			print ('С телегой что-то не так')




Tiger = Tank('Tiger')

T34 = Tank('T34')
T34.shassi = False
BMW = Car('BMW')

Audi = Car ('Audi')
Audi.speed = 90

Telega = Telega()

cars = [Tiger,T34,BMW,Audi,Telega]

for i in cars:
	i.status()
