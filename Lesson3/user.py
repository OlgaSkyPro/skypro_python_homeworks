class User:
	
	def __init__(self, first_name, last_name):
		self.username = last_name
		self.username2 = first_name

	def print_name(self):
		print("меня зовут ", self.username2)

	def print_name2(self):
		print("моя фамилия  ", self.username)
		
	def print_full_name(self):
         print("мои имя и фамилия  ", self.username2, end=' '), print (self.username)


#ivan = User("Ivan", "Ivanov")


#ivan.PrintName()
#ivan.PrintName2()
#ivan.PrintFullName()