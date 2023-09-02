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
        pass
        
    def borrar_alumno(self,id):
        pass
    
    def actualizar_alumno(self,id):
        pass
    def cerrar_conexion(self):
        self.conexion.close()        



        


# ejecutamos el menu     


menu()
alumno = Alumno("Jose", " Calixto", 1995, 2020,4)
#print(alumno)
alumno.iniciar_conexion("alumnos.db")
alumno.crear_tablas()
#alumno.crear_alumno()
print(alumno.ver_alumnos())

