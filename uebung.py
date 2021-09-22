daten = 'Device1:152.96.1.1:vlan230,Device2:152.96.2.1:vlan240,Device3:152.96.3.1:vlan250'
einzeldaten = daten.split(",")
einzeldaten2 = daten.split(":")
for i in einzeldaten2:
    print(i)

#print(einzeldaten[1])
#Device1:152.96.1.1:vlan230,Device2:152.96.1.2:vlan231,Device3:152.96.1.3:vlan232