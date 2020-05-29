# -*- coding: utf-8 -*-

import sqlite3
import random

### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

temp4=0
temp3=0
temp2=0
temp1=0
temp0=0
humedad4=0
humedad3=0
humedad2=0
humedad1=0
humedad0=0
presion4=0
presion3=0
presion2=0
presion1=0
presion0=0
st4=0
st3=0
st2=0
st1=0
st0=0

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hola usuarios!")
    return dict(message=T('Welcome to web2py!'))

def error():
    return dict()

def registro_clima_manage():
    form = SQLFORM.smartgrid(db.t_registro_clima,onupdate=auth.archive)
    return locals()

def actual_manage():
    return dict()
  
def pide_datos():
    global temp4
    global temp3
    global temp2
    global temp1
    global temp0
    global humedad4
    global humedad3
    global humedad2
    global humedad1
    global humedad0
    global presion4
    global presion3
    global presion2
    global presion1
    global presion0
    global st4
    global st3
    global st2
    global st1
    global st0
            
    con=sqlite3.connect('C:\Users\Marcelo\Desktop\PRUEBAS\storage.sqlite')

    cursor = con.cursor()
    
    a=0

    cursor.execute("SELECT temperatura FROM t_registro_clima order by id desc LIMIT 5")

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
    cursor.execute("SELECT humedad FROM t_registro_clima order by id desc LIMIT 5")

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
    cursor.execute("SELECT fechahora FROM t_registro_clima order by id desc LIMIT 5")

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
                    fechahora4=i[0]
            a=a+1

    a=0
    cursor.execute("SELECT sensacion_termica FROM t_registro_clima order by id desc LIMIT 5")

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
    cursor.execute("SELECT presion FROM t_registro_clima order by id desc LIMIT 5")

    for i in cursor:
            
            if a==0:
                    presion0=i[0]
            if a==1:
                    presion1=i[0]
            if a==2:
                    presion2=i[0]
            if a==3:
                    presion3=i[0]
            if a==4:
                    presion4=i[0]
            a=a+1

    print temp4, temp3, temp2, temp1, temp0
    print humedad4, humedad3, humedad2, humedad1, humedad0
    print presion4, presion3, presion2, presion1, presion0
    print st4, st3, st2, st1, st0
    
    
##@service.json
def series_temp():
    global temp4
    global temp3
    global temp2
    global temp1
    global temp0
    
    temp4=0
    temp3=5
    temp2=2
    temp1=6
    temp0=10
    
    s = '{"series":[['
    
    flotante = temp4
    s = s + "%d, " % (flotante)
    flotante = temp3
    s = s + "%d, " % (flotante)
    flotante = temp2
    s = s + "%d, " % (flotante)
    flotante = temp1
    s = s + "%d, " % (flotante)
    flotante = temp0
    s = s + "%d, " % (flotante)

    s = s[:-2] + ']]}'    
    #return '{"series":[[0, 9, 1, 8, 2, 7, 3, 6, 4, 5, 6, 6]]}'
    print s
    return s

##@service.json
def series_hume():
    global humedad4
    global humedad3
    global humedad2
    global humedad1
    global humedad0
    
    s = '{"series":[['
    
    flotante = float(humedad4)
    s = s + "%f, " % (flotante)
    flotante = float(humedad3)
    s = s + "%f, " % (flotante)
    flotante = float(humedad2)
    s = s + "%f, " % (flotante)
    flotante = float(humedad1)
    s = s + "%f, " % (flotante)
    flotante = float(humedad0)
    s = s + "%f, " % (flotante)

    s = s[:-2] + ']]}'
    print s
    return s
  
##@service.json    
def series_presion():
    global presion4
    global presion3
    global presion2
    global presion1
    global presion0
    
    s = '{"series":[['
    
    flotante = float(presion4)
    s = s + "%f, " % (flotante)
    flotante = float(presion3)
    s = s + "%f, " % (flotante)
    flotante = float(presion2)
    s = s + "%f, " % (flotante)
    flotante = float(presion1)
    s = s + "%f, " % (flotante)
    flotante = float(presion0)
    s = s + "%f, " % (flotante)

    s = s[:-2] + ']]}'
    print s
    return s

##@service.json
def series_st():
    global st4
    global st3
    global st2
    global st1
    global st0
    
    s = '{"series":[['
    
    flotante = float(st4)
    s = s + "%f, " % (flotante)
    flotante = float(st3)
    s = s + "%f, " % (flotante)
    flotante = float(st2)
    s = s + "%f, " % (flotante)
    flotante = float(st1)
    s = s + "%f, " % (flotante)
    flotante = float(st0)
    s = s + "%f, " % (flotante)

    s = s[:-2] + ']]}'
    print s
    return s
  
pide_datos()
series_temp()
series_hume()
series_presion()
series_st()
