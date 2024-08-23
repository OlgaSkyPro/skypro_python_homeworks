from adress import Address
from mailing import Mailing

to_address = Address ("100000", "Moscow", "Tverskaya", "10", "1")
from_address = Address ("100001", "Moscow", "Tverskaya", "11", "13")
mailing = Mailing (to_address, from_address, 100, "XXXXXX")

print ("Отправление: ", mailing.track, end=' '), print ("из ", mailing.from_addres.index, end=' ') 
print (mailing.from_addres.city, end= " ")
print (mailing.from_addres.street, end =" ")
print (mailing.from_addres.home, end =" ")
print (mailing.from_addres.app, end =" ")
print ("в ", mailing.to_address.index, end=' ') 
print (mailing.to_address.city, end= " ")
print (mailing.to_address.street, end =" ")
print (mailing.to_address.home, end =" ")
print (mailing.to_address.app, end =" ")
print ("Стоимость", mailing.cost)