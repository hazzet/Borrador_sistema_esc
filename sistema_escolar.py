import sqlite3

# este es un borrador para el proyecto del sistema escolar

def menu():
    print("""
1._ agregar alumno
2._ver alumnos
3._ver alumno
4._eliminar alumno
5._salir
    """)

class Alumno:
    def __init__(self,nombre,apellido,año_de_nacimiento,fecha_de_ingreso,grado_escolar) -> None:
        
        self.nombre = nombre
        self.apellido = apellido
        self.año_de_nacimiento = año_de_nacimiento
        self.fecha_de_ingreso = fecha_de_ingreso
        self.grado_escolar = grado_escolar
        
    def __str__(self) -> str:
        return (f"{self.nombre} {self.apellido} {self.año_de_nacimiento}")

# creamos el crud para la base de datos 
    def iniciar_conexion(self, db_alumnos) -> None:
        self.conexion = sqlite3.connect(db_alumnos)
        self.cursor = self.conexion.cursor()
        
    def crear_tablas(self):    
        self.cursor.execute ("""
            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                apellido TEXT,
                año_de_nacimiento INTEGER ,
                fecha_de_ingreso TEXT,
                grado_escolar INTEGER   
                    )
               """)
        self.conexion.commit()
        
        
    def crear_alumno(self):
        self.cursor.execute(""" 
            INSERT INTO alumnos (nombre, apellido, año_de_nacimiento,
                fecha_de_ingreso,grado_escolar)
                VALUES (?,?,?,?,?)""",
                (self.nombre, self.apellido, self.año_de_nacimiento,self.fecha_de_ingreso,self.grado_escolar))
        self.conexion.commit()
    def ver_alumnos(self):
        self.cursor.execute("""
        SELECT * FROM alumnos                    
                            """)
        self.conexion.commit()
        return self.cursor.fetchall()
        
    def ver_alumno(self, id):
        self.cursor.execute("""
        SELECT * FROM maestros                    
                            """)
        self.conexion.commit()
        return self.cursor.fetcone(id)
        
    def borrar_alumno(self,id,nuevo_nombre,nuevo_apellido,nueva_fecha_nacimiento,nueva_fecha_ingreso,):
        self.cursor.execute("DELETE FROM alumnos WHERE id = ?", (id,))
        self.conexion.commit()
    def actualizar_alumno(self,id):
        pass
    def cerrar_conexion(self):
        self.conexion.close()        
        
class Mestro:
    def __init__(self,nombre,apellido,año_de_nacimiento,fecha_de_ingreso) -> None:
        
        self.nombre = nombre
        self.apellido = apellido
        self.año_de_nacimiento = año_de_nacimiento
        self.fecha_de_ingreso = fecha_de_ingreso
        
    def __str__(self) -> str:
        return (f"{self.nombre} {self.apellido} {self.año_de_nacimiento}")

# creamos el crud para la base de datos 
    def iniciar_conexion(self, db_maestros) -> None:
        self.conexion = sqlite3.connect(db_maestros)
        self.cursor = self.conexion.cursor()
        
    def crear_tablas(self):    
        self.cursor.execute ("""
            CREATE TABLE IF NOT EXISTS maestros (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                apellido TEXT,
                año_de_nacimiento INTEGER ,
                fecha_de_ingreso TEXT   
                    )
               """)
        self.conexion.commit()
        
        
    def crear_alumno(self):
        self.cursor.execute(""" 
            INSERT INTO maestros (nombre, apellido, año_de_nacimiento,
                fecha_de_ingreso)
                VALUES (?,?,?,?,?)""",
                (self.nombre, self.apellido, self.año_de_nacimiento,self.fecha_de_ingreso))
        self.conexion.commit()
    
    def ver_maestros(self):
        self.cursor.execute("""
        SELECT * FROM maestros                    
                            """)
        self.conexion.commit()
        return self.cursor.fetchall()
        
    def ver_maestro(self, id):
        self.cursor.execute("""
        SELECT * FROM maestros                    
                            """)
        self.conexion.commit()
        return self.cursor.fetchone(id)
        
    def borrar_maestro(self,id):
        self.cursor.execute("DELETE FROM mestros WHERE id = ?", (id,))
        self.conexion.commit()
    def actualizar_maestro(self,id,nuevo_nombre,nuevo_apellido,nueva_fecha_nacimiento,):
        pass
    def cerrar_conexion(self):
        self.conexion.close()           


# ejecutamos el menu 

while(True):
    menu()
    opcion = int(input("Ingresa Una Opción."))
    if opcion == 1:pass
    elif opcion == 2:pass
    elif opcion == 3: pass
    elif opcion == 4: pass
    elif opcion == 5: exit()
    else: print("Opcion Invalida Reintente Por favor.")
        
    

