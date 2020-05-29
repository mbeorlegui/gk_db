#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sqlite3
import time

con = sqlite3.connect('storage.sqlite')

cur = con.cursor()

direccion = ""
puerto = 9138

s = socket.socket()

s.bind(( direccion, puerto))

while True:
	s.listen(1)

	sc, addr = s.accept()

	err = 0
	while True:
		try:
		#if True:
			recibido = sc.recv(1024)
	  
			if recibido == "exit":
				err = 0
				break
	  
			if recibido == "":
				sc.close()
				break

			print "Recibido:", recibido	
			
			if len(recibido) > 0:
				try:
					cur = con.cursor()
					qry = """insert into t_registro_clima
								(temperatura, 
								 humedad, 
								 sensacion_termica,
								 velocidad_viento,
								 direccion_viento,
								 indice_uv,
								 cantidad_lluvia,
								 presion,
								 fechahora)  
							values (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
					
					aux = recibido
					aux = aux.split(";")
					te = float(aux[0][1:])/10
					hu = aux[1][1:]
					st = aux[2][2:]
					vv = aux[3][2:]
					dv = aux[4][2:]
					uv = aux[5][2:]
					cl = aux[6][2:]
					pr = aux[7][2:]

					
					fechahora = time.strftime("%Y-%m-%d") + " "
					fechahora = fechahora + time.strftime("%H:%M:%S")
					
					cur.execute(qry, (te, hu, st, vv, dv, uv, cl, pr, fechahora))
					con.commit()
					
				except:
					print("Error de base de datos")
					
		
		except:
			sc.close()  
			err = 1
			break 
		
if err == 0:
	sc.close()
	s.close()
	conn.close()
