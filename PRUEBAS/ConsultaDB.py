import sqlite3

global temp4
global temp3
global temp2
global temp1
global temp0

con=sqlite3.connect('C:\Users\Marcelo\Desktop\PRUEBAS\storage.sqlite')

cursor = con.cursor()



a=0

cursor.execute("SELECT temperatura FROM t_registro_clima LIMIT 5")

for i in cursor:
	
	if a==0:
		temp0=i[0]
	if a==1:
		temp1=i[0]
	if a==2:
		temp2=i[0]
	if a==3:
		temp3=i[0]
	if a==4:
		temp4=i[0]
	a=a+1

a=0
cursor.execute("SELECT humedad FROM t_registro_clima LIMIT 5")

for i in cursor:
	
	if a==0:
		humedad0=i[0]
	if a==1:
		humedad1=i[0]
	if a==2:
		humedad2=i[0]
	if a==3:
		humedad3=i[0]
	if a==4:
		humedad4=i[0]
	a=a+1

a=0
cursor.execute("SELECT fechahora FROM t_registro_clima LIMIT 5")

for i in cursor:
	
	if a==0:
		fechahora0=i[0]
	if a==1:
		fechahora1=i[0]
	if a==2:
		fechahora2=i[0]
	if a==3:
		fechahora3=i[0]
	if a==4:
		fechahora=i[0]
	a=a+1

a=0
cursor.execute("SELECT sensacion_termica FROM t_registro_clima LIMIT 5")

for i in cursor:
	
	if a==0:
		st0=i[0]
	if a==1:
		st1=i[0]
	if a==2:
		st2=i[0]
	if a==3:
		st3=i[0]
	if a==4:
		st4=i[0]
	a=a+1

a=0
cursor.execute("SELECT presion FROM t_registro_clima LIMIT 5")

for i in cursor:
	
	if a==0:
		presion0=i[0]
	if a==1:
		presion1=i[0]
	if a==2:
		presion2=i[0]
	if a==3:
		presion=i[0]
	if a==4:
		presion4=i[0]
	a=a+1

