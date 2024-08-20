class User:
	
	def __init__(self, first_name, last_name):
		self.username = last_name
		self.username2 = first_name

	def PrintName(self):
		print("меня зовут ", self.username2)

	def PrintName2(self):
		print("моя фамилия  ", self.username)
		
	def PrintFullName(self):
         print("мои имя и фамилия  ", self.username2, end=' '), print (self.username)


