# Clase 5 Programacion Avanzada: BBDD

import sqlite3

def crear_conexion():
    try:
        con = sqlite3.connect("./mydatabase5.db")
        print("Se ha creado la BBDD")
        return con
    except sqlite3.Error as e:
        print("Ha ocurrido un error: ", e)
        

def crear_tabla(con):
    try:
        my_cursor = con.cursor()
        my_cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (dni varchar(10) UNIQUE, nombre varchar(100))")
        con.commit()
        #con.close()
        print("Se ha creado la tabla")
    except sqlite3.Error as e:
        print("Ha ocurrido un error: ", e)  
    
def crear_registro(con):
    try:
        my_cursor = con.cursor()
        my_cursor.execute("insert into alumnos (dni, nombre) values ('230340', 'Pedro')")
        con.commit()
        #con.close()
        print("El nombre ha sido insertado")
    except sqlite3.Error as e:
        print("Ha ocurrido un error: ", e)  

def seleccionar_rows(con):
    try:
        my_cursor = con.cursor()
        my_cursor.execute("select * from alumnos")
        con.commit()
        #con.close()
        rows = my_cursor.fetchall()
        print(rows)
    except sqlite3.Error as e:
        print("Ha ocurrido un error: ", e)  


con = crear_conexion()
crear_tabla(con)
crear_registro(con)
seleccionar_rows(con)

# A partir de aqui es de la clase extra 3:

