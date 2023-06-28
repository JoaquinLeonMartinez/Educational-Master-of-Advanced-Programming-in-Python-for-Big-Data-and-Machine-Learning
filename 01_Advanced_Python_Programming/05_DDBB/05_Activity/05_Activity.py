'''
Author: Joaquin Leon Martinez

Crea en Python una función que genere una BBDD Sqlite3
Partiendo de la BBDD generada, crea una función que genere las siguientes tablas:
• Una tabla con 4 campos
• Una tabla con 2 campos
Crea una función para cada una de las siguientes sentencias que opere sobre las tablas creadas:
• Insertar
• Actualizar
• Listar
• Borrar
'''

import sqlite3
'''
Clases que seran necesarias:
'''
class alumno:
    def __init__(self,nombre,  dni):
        try:
            self.nombre = nombre
            self.dni = dni
        except Exception as e:
            print("Ha ocurrido un error", e)
            
class profesor:
    def __init__(self,nombre, apellido,  dni, asignatura):
        try:
            self.nombre = nombre
            self.apellido = apellido
            self.dni = dni
            self.asignatura = asignatura
        except Exception as e:
            print("Ha ocurrido un error", e)


'''
Crea en Python una función que genere una BBDD Sqlite3
'''
def crear_conexion():
    try:
        con = sqlite3.connect("./mydatabase.db")
        print("Se ha creado la BBDD")
        return con
    except sqlite3.Error as e:
        print("Error: ", e)
        
'''
Partiendo de la BBDD generada, crea una función que genere las siguientes tablas:
• Una tabla con 4 campos
• Una tabla con 2 campos
'''
def crear_tabla(con): # Como posible mejora yo indicaria el string de la query por parametro
    try:
        tabla1 = '''
            create table if not exists alumnos(
                nombre varchar(100),
                dni varchar(10) primary key
            )
        
        '''
        tabla2 = '''
            create table if not exists profesores(
                nombre varchar(100),
                apellido varchar(100),
                dni varchar(10) primary key,
                asignatura varchar(25)
            )
        '''
        cursor = con.cursor()
        cursor.execute(tabla1)
        cursor.execute(tabla2)
        con.commit()
        print("Se han creado las tablas")
    except sqlite3.Error as e:
        print("Error: ", e)  
              
'''
• Insertar
'''
def insertar(con, tabla, registro): # Se indica en que tabla se va a insertar el registro
    try:
        keys = ""
        values = ""
        
        for index in registro.__dict__:
            keys += index + ","
            # Habria que comprobar el tipo de dato si quisieramos meter algo que no sea VARCHAR (que no es el caso)
            values += "'" + registro.__dict__.get(index) + "'," 
        
        # Eliminamos la ultima ',' para que la sinsaxis sea correcta
        keys = keys[:-1]
        values = values[:-1]
        
        #print("Keys:", keys)    
        #print("Values:", values)    
        
        sql = f"insert into {tabla} ({keys}) values ({values})"
        #print("Query:", sql)
        
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("El registro se ha insertado")
    except sqlite3.Error as e:
        print("Error: ", e)

'''
• Actualizar
'''
def actualizar_registro(con, tabla, registro):
    try:
        my_cursor = con.cursor()
        
        #SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
        values = ""
        key_value = ""
        
        for index in registro.__dict__:
            values += index + " = '" + registro.__dict__.get(index) + "'," 
            if index == "dni":
                key_value = "'" + registro.__dict__.get(index) + "'"
        
        # Eliminamos la ultima ',' para que la sinsaxis sea correcta
        values = values[:-1]
        #print(values)
        #print(sql)
        sql = f"update {tabla} set {values} where dni = {key_value}"
        
        my_cursor.execute(sql)
        con.commit()
    except sqlite3.Error as e:
        print("Ha ocurrido un error: ", e)  

'''
• Listar
'''
def listar_tabla(con, tabla):
    try:
        my_cursor = con.cursor()
        my_cursor.execute(f"select * from {tabla}")
        con.commit()
        rows = my_cursor.fetchall()
        print(rows)
    except sqlite3.Error as e:
        print("Ha ocurrido un error: ", e)  

'''
• Borrar
'''
def eliminar_registro(con, tabla, dni): # Eliminamos siempre por DNI
    try:
        my_cursor = con.cursor()
        my_cursor.execute(f"delete from {tabla} where dni = '{dni}'")
        con.commit()
    except sqlite3.Error as e:
        print("Ha ocurrido un error: ", e)  



alumno1 = alumno("Pedro", "123131D")
alumno2 = alumno("Maria", "156131D")
profesor1 = profesor("Mariano", "Garcia", "143631D", "Lengua")
profesor2 = profesor("Carmen", "Soledad", "999131D", "Geografia")

con = crear_conexion()
crear_tabla(con)


insertar(con, "alumnos", alumno1)
insertar(con, "alumnos", alumno2)
insertar(con, "profesores", profesor1)
insertar(con, "profesores", profesor2)

listar_tabla(con, "alumnos")
listar_tabla(con, "profesores")

eliminar_registro(con, "alumnos", "123131D")
listar_tabla(con, "alumnos")

eliminar_registro(con, "profesores", "143631D")
listar_tabla(con, "profesores")

alumno2.nombre = "Hulio"
actualizar_registro(con, "alumnos", alumno2)
listar_tabla(con, "alumnos")

profesor2.nombre = "Hulia"
actualizar_registro(con, "profesores", profesor2)
listar_tabla(con, "profesores")

