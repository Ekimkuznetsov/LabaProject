"""
Задание 6.1
Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании cisco MAC-адреса
используются в формате XXXX.XXXX.XXXX.
Создать скрипт, который преобразует MAC-адреса в формат cisco и добавляет их в новый список mac_cisco
Ограничение: Все задания надо выполнять используя только пройденные темы.
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
"""

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
#Convert to string, apply replace(), add to new list
for address in mac:
    new_address = address.replace(":", ".")
    if mac_cisco == None:
        mac_cisco.insert(0, new_address)
    else:
        mac_cisco.append(new_address)


print(mac_cisco)

#Task 2
"""
Задание 6.2 
1.Запросить у пользователя ввод IP-адреса в формате 10.0.1.1 
2.Определить тип IP-адреса. 3.В зависимости от типа адреса, 
вывести на стандартный поток вывода: 
•„unicast“ - если первый байт в диапазоне 1-223 
•„multicast“ - если первый байт в диапазоне 224-239 
•„local broadcast“ - если IP-адрес равен 255.255.255.255 
•„unassigned“ - если IP-адрес равен 0.0.0.0 
•„unused“ - во всех остальных случаях 
Ограничение: Все задания надо выполнять используя только пройденные темы. 
"""

#Ввод адреса в формате 10.0.0.1 0-255 max
#address = input("Print address here in format 0.0.0.0: " )
#if address == 0.0.0.0
#print(address)

import re
#Address input and check
ip_address = input('Enter IP Address: ')
if not re.match(r'[0-9]+(\.[0-9]+){3}', ip_address):
    print('Invalid IP Address')
print(ip_address)
#Type determination
#bits separation
new_address = ip_address.split(".")

if int(new_address[0]) > 0 and int(new_address[0]) < 224:
    print("Unicast")
elif int(new_address[0]) > 223 and int(new_address[0]) < 240:
    print("Multicast")
elif (ip_address) == "255.255.255.255":
    print("Local brodcast")
elif (ip_address) == "0.0.0.0":
    print("unassigned")
else:
    print("Address out of usible range")
