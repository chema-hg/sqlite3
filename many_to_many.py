import sqlite3

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('universidad.db')
cursor = conn.cursor()

# Crear la tabla de Estudiantes
cursor.execute('''CREATE TABLE estudiantes (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT)''')

# Crear la tabla de Cursos
cursor.execute('''CREATE TABLE cursos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT)''')

# Crear la tabla intermedia para la relación many-to-many
cursor.execute('''CREATE TABLE inscripciones (
                    estudiante_id INTEGER,
                    curso_id INTEGER,
                    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
                    FOREIGN KEY (curso_id) REFERENCES cursos(id),
                    PRIMARY KEY (estudiante_id, curso_id))''')

# Insertar datos
cursor.execute("INSERT INTO estudiantes (nombre) VALUES ('Alice')")
cursor.execute("INSERT INTO estudiantes (nombre) VALUES ('Bob')")
cursor.execute("INSERT INTO cursos (nombre) VALUES ('Matemáticas')")
cursor.execute("INSERT INTO cursos (nombre) VALUES ('Historia')")
cursor.execute("INSERT INTO inscripciones (estudiante_id, curso_id) VALUES (1, 1)")  # Alice está inscrita en Matemáticas
cursor.execute("INSERT INTO inscripciones (estudiante_id, curso_id) VALUES (1, 2)")  # Alice está inscrita en Historia
cursor.execute("INSERT INTO inscripciones (estudiante_id, curso_id) VALUES (2, 1)")  # Bob está inscrito en Matemáticas

# Consulta para obtener todos los estudiantes inscritos en un curso específico (por ejemplo, Matemáticas)
cursor.execute("SELECT estudiantes.nombre FROM estudiantes JOIN inscripciones ON estudiantes.id = inscripciones.estudiante_id JOIN cursos ON inscripciones.curso_id = cursos.id WHERE cursos.nombre = 'Matemáticas'")
estudiantes_matematicas = cursor.fetchall()
print("Estudiantes inscritos en Matemáticas:")
for estudiante in estudiantes_matematicas:
    print(estudiante[0])

# Cerrar la conexión
conn.commit()
conn.close()
