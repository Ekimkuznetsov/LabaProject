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
# Convert to string, apply replace(), add to new list
for address in mac:
    new_address = address.replace(":", ".")
    if mac_cisco == None:
        mac_cisco.insert(0, new_address)
    else:
        mac_cisco.append(new_address)
print(mac_cisco)

#Task 2b 6.2
#Ввод адреса в формате 10.0.0.1 0-255 max

import re
#Address input
#ip_address = input('Enter IP Address: ') locally



#The function to check correct address and request assigning function
def address_check():
    ip_address = input('Enter IP Address in format 0.0.0.0: ')
    new_address = ip_address.split(".")
    if not re.match(r'[0-9]+(\.[0-9]+){3}', ip_address):
        print('Неправильный IP-адрес')
        return address_check()
    else:
        for index in range(4):
            if int(new_address[index]) > 255:
                print("Out of range")
                return address_check()

    print(ip_address)
    address_assign(ip_address)
#assigning function
def address_assign(func):
    new_address = func.split(".") #Creating a list of digited parts
    if int(new_address[0]) > 0 and int(new_address[0]) < 224:
        print("Unicast")
    elif int(new_address[0]) > 223 and int(new_address[0]) < 240:
        print("Multicast")
    elif (func) == "255.255.255.255":
        print("Local broadcast")
    elif (func) == "0.0.0.0":
        print("unassigned")
    else:
        print("Address free to use")

address_check()


#Task 6.3 Lab2b

access_template = [
'switchport mode access', 'switchport access vlan',
'spanning-tree portfast', 'spanning-tree bpduguard enable'
]
trunk_template = [
'switchport trunk encapsulation dot1q', 'switchport mode trunk',
'switchport trunk allowed vlan'
]
access = {
'0/12': '10',
'0/14': '11',
'0/16': '17',
'0/17': '150'
}
trunk = {
'0/1': ['add', '10', '20'],
'0/2': ['only', '11', '30'],
'0/4': ['del', '17']
}
for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

for intf, vlan in trunk.items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if vlan[0] == 'add':
                print(" switchport trunk allowed vlan add {},{}".format(vlan[1], vlan[2]))
            elif vlan[0] == 'del':
                print(" switchport trunk allowed vlan remove {}".format(vlan[1]))
            elif vlan[0] == 'only':
                print(" switchport trunk allowed vlan {},{}".format(vlan[1], vlan[2]))
        else:
            print(' {}'.format(command))
