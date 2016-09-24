# -*- coding: utf-8 -*-
# Importamos la libreria de SQLite
import sqlite3

# Creamos la conexion
connection = sqlite3.connect('test.db')

# Creamos el cursor
cursor = connection.cursor()

# Creamos el arreglo que contiene toda la informacion
datos = [
    ('Pedro Perez', 34, 'pperez@tucorreo.com', '', 4),
    ('Maria Gomez', 25, 'maria@sucorreo.com', '', 7),
    ('Pablo Rodriguez', 41, 'pablor@elcorreo.com', 'www.pablo.com', 3),
]

# Insertamos todos los registros
for t in datos:
    cursor.execute('INSERT INTO Usuarios (nombre,edad,correo,url,visitas) VALUES (?,?,?,?,?)', t)

# Hacemos efectiva la transaccion
connection.commit()

# Imprimimos todos los registros
print("\nLista de todos los registros de la base de datos:")
cursor.execute('SELECT * FROM Usuarios')
for row in cursor:
    print(row)

# Imprimimos solo el registro que tenga id = 1
id = (1, )
cursor.execute("SELECT nombre, visitas FROM Usuarios WHERE id=?", id)
for row in cursor:
    print("\n%s ha realizado %i visitas" % (row[0], row[1]))

# Actualizamos la edad de Pablo
values = (24, 'pablor@elcorreo.com', )
cursor.execute("UPDATE Usuarios SET edad=? WHERE correo=?", values)
connection.commit()
print("\nActualizada la edad de Pablo")

# Y volvemos a imprimir todos los registros para verificar los cambios
print("\nRegistros de la base de datos despues de actualizar a Pablo:")
cursor.execute('SELECT * FROM Usuarios')
for row in cursor:
    print(row)

# Borramos todos los registros con edades mayores de 34 anios
value = (34,)
cursor.execute("DELETE FROM Usuarios WHERE edad >= ?", value)
connection.commit()
print("\nBorrados todos los ancianos ;)")

# E imprimimos otra vez todos los registros para verificar los cambios
print("\nRegistros de la base de datos despues de borrar a los viejitos:")
cursor.execute('SELECT * FROM Usuarios')
for row in cursor:
    print(row)

# Finalmente cerramos todo como debe ser
cursor.close()
connection.close()