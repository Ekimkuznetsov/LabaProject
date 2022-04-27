#Task1.1
#Default string
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT1 = NAT.replace("Fast", "Gigabit")
print(NAT1)

#Task1.2
#Default string convert to "b"
mac = 'AAAA:BBBB:CCCC'
print(mac.replace(':', '.'))

#Task1.3
#Default string. Reject VLANs
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config1 = config.split(" ")
vlans = config1[-1].split(",")
print(vlans)

#Task1.4
#Default string. Reject VLANs sorted without repitations
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

vlans1 = list()
for vlan in vlans:
    if vlan in vlans1:
        continue
    vlans1.append(vlan)
print(sorted(vlans1))

#Alternative 1.4
a = set(vlans)
result = sorted(list(a))
print(result)

#Task1.5
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
command1set = command1.split(" ")
vlans1 = set(command1set[-1].split(","))
command2set = command2.split(" ")
vlans2 = set(command2set[-1].split(","))
result = sorted(list(vlans1.intersection(vlans2)))
print(result)

#Task1.6
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
def cleaner():
    pass
ospf_route = ospf_route.replace('[', '')
ospf_route = ospf_route.replace(']', '')
ospf_route = ospf_route.replace(',', '')
print(ospf_route)

def splitter():
    pass
listed_info = ospf_route.split(" ")

result = {'Protocol' : "OSPF", 'Prefix' : listed_info[1],
              'AD/Metric' : listed_info[2], 'Next-Hop' : listed_info[4],
              'Last update' : listed_info[5], 'Outbound' : listed_info[6],
              'interface' : ' '}
for key in result:
    print(key, ':' , result[key])

#Task1.7
mac = 'AAAA:BBBB:CCCC'
macc = "A"
#Clean the data
mac = mac.replace(":", "")
#Separation
bin_simbol = ""
for simbol in mac:
    bin_simbol = bin_simbol + bin(int(simbol, 16)).replace('0b', '')
#Concatenation
print(bin_simbol)

#Task1.8
"""
Задание 8
Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод
столбцами, таким образом:
• первой строкой должны идти десятичные значения байтов
• второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
• столбцами
• ширина столбца 10 символов
Пример вывода для адреса 10.1.1.1:
10 1 1 1
00001010 00000001 00000001 00000001
Ограничение: Все задания выполнять используя только пройденные темы.
"""
ip = '192.168.3.1'
ip = ip.split(".")
print(ip)
ip_template = ''' {0:<10} {1:<10} {2:<10} {3:<10}
{0:010b} {1:010b} {2:010b} {3:010b}
'''
print(ip_template.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))
