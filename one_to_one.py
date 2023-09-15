import sqlite3

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear la tabla de Usuarios
cursor.execute('''CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT)''')

# Crear la tabla de Información de Contacto
cursor.execute('''CREATE TABLE informacion_contacto (
                    id INTEGER PRIMARY KEY,
                    email TEXT UNIQUE,
                    usuario_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''')

# Insertar datos
cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Alice')")
cursor.execute("INSERT INTO informacion_contacto (email, usuario_id) VALUES ('alice@example.com', 1)")

# Consulta para obtener el correo electrónico de un usuario específico (por ejemplo, Alice)
cursor.execute("SELECT informacion_contacto.email FROM informacion_contacto JOIN usuarios ON informacion_contacto.usuario_id = usuarios.id WHERE usuarios.nombre = 'Alice'")
correo_alice = cursor.fetchone()
print("Correo electrónico de Alice:", correo_alice[0])

# Cerrar la conexión
conn.commit()
conn.close()
