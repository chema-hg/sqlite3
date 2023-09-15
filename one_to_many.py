import sqlite3

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Crear la tabla de Autores
cursor.execute('''CREATE TABLE autores (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT)''')

# Crear la tabla de Libros
cursor.execute('''CREATE TABLE libros (
                    id INTEGER PRIMARY KEY,
                    titulo TEXT,
                    autor_id INTEGER,
                    FOREIGN KEY (autor_id) REFERENCES autores(id))''')

# Insertar datos
cursor.execute("INSERT INTO autores (nombre) VALUES ('J.K. Rowling')")
cursor.execute("INSERT INTO libros (titulo, autor_id) VALUES ('Harry Potter y la piedra filosofal', 1)")
cursor.execute("INSERT INTO libros (titulo, autor_id) VALUES ('Harry Potter y la cámara secreta', 1)")

# Consulta para obtener todos los libros de un autor específico (por ejemplo, J.K. Rowling)
cursor.execute("SELECT libros.titulo FROM libros JOIN autores ON libros.autor_id = autores.id WHERE autores.nombre = 'J.K. Rowling'")
libros_jk_rowling = cursor.fetchall()
print("Libros de J.K. Rowling:")
for libro in libros_jk_rowling:
    print(libro[0])

# Cerrar la conexión
conn.commit()
conn.close()