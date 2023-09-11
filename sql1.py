import sqlite3

with sqlite3.connect('base.db') as conexion:
    # Si queremos crear la base de datos en la memoria usamos como
    # nombre de la base de datos ':memory:'
    
    # Creamos el cursor
    c = conexion.cursor()
    # Creamos las tablas
    c.execute('''
            CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT Null,
            name VARCHAR(255) NOT Null            
            )''')
    c.execute('''
            CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT Null,
            key VARCHAR(255) NOT Null,
            start_at DATE NOT Null,
            end_at DATE)''')
    c.execute('''
            CREATE TABLE IF NOT EXISTS events_teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT Null,
            event_id INTEGER NOT Null,
            team_id INTEGER NOT Null,
            FOREIGN KEY(event_id) REFERENCES events (id),
            FOREIGN KEY(team_id) REFERENCES teams (id))''')
    
# DATE es solo la fecha
# DATETIME es fecha mas hora precisa
    c.execute('''
            CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT Null,
            event_id INTEGER NOT Null,
            round VARCHAR(255) NOT NULL,
            team1_id INTEGER NOT Null,
            team2_id INTEGER NOT Null,
            play_at DATETIME NOT Null,
            score1 INTEGER,
            score2 INTEGER,
            winner INTEGER,
            FOREIGN KEY(event_id) REFERENCES events(id),
            FOREIGN KEY(team1_id) REFERENCES teams(id),
            FOREIGN KEY(team2_id) REFERENCES teams(id))''')
    c.execute('''
            CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT Null,
            key VARCHAR(255) NOT Null,
            title VARCHAR(255) NOT Null,
            country_id INTEGER NOT Null,
            FOREIGN KEY(country_id) REFERENCES countries (id))''')
    
#     En este código, hemos agregado la restricción de clave externa FOREIGN KEY (country_id) REFERENCES countries (id)
#     al campo "country_id" de la tabla "teams." Esto establece una relación de clave externa entre "country_id" en la
#     tabla "teams" y "id" en la tabla "countries."
# 
#     Esto significa que el valor en "country_id" en la tabla "teams" debe coincidir con un valor existente en la
#     columna "id" de la tabla "countries." Esto garantiza que solo se pueden insertar valores válidos en "country_id"
#     que correspondan a países existentes en la tabla "countries."
    
    c.execute('''INSERT INTO countries VALUES(63, 'China')''')
    
    # En SQLite, para representar un valor nulo, debes utilizar None en lugar de NULL
    # pero si lo hacemos de la siguiente forma para introducir los datos.
    data_to_insert = [
    (109, 'Germany'),
    (None, 'Estonia'),
    (None, 'Spain'),
    (None, 'Finland'),
    (None, 'France'),
    (None, 'Greece'),
    (None, 'Irland'),
    (None, 'Italy'),
    (120, 'Portugal'),
    (127, 'Poland'),
    (186, 'Argentina'),
    (194, 'Uruguay'),
    # Utiliza None en lugar de NULL para representar un valor nulo.
    ]
    # La función executemany() en SQLite se utiliza principalmente para insertar múltiples
    # filas de datos en una tabla, no para crear tablas o definir su estructura
    c.executemany('INSERT INTO countries VALUES (?, ?)', data_to_insert)
    
    # Creando filas para events
    data_to_insert = [
        (None, 'world.1930','1930-07-13', None),
        (None, 'world.1934','1934-05-27', None),
        (None, 'world.1938','1938-06-04', None),
        (None, 'world.1950','1950-06-24', None),
        (None, 'world.1954','1954-06-16', None),
        (None, 'world.1958','1958-06-08', None),
        (None, 'world.1962','1962-05-30', None),
        (None, 'world.1966','1966-07-11', None),
        (None, 'world.1970','1970-05-31', None),
        (None, 'world.1974','1974-06-13', None),
        (None, 'world.1978','1978-05-01', None),
        (None, 'world.1982','1982-06-13', None),
        (None, 'world.1986','1986-05-31', None),
        (None, 'world.1990','1990-06-08', None),
        (None, 'world.1994','1994-06-17', None),
        (None, 'world.1998','1998-06-10', None),
        (None, 'world.2002','2002-05-31', None),
        (None, 'world.2006','2006-06-09', None),
        (None, 'world.2010','2010-06-11', None),
        (None, 'world.2014','2014-06-12', None),
        
        ]
    
    c.executemany('INSERT INTO events VALUES (?, ?, ?, ?)', data_to_insert)
    
    # Creando filas para teams
    data_to_insert = [
        (70, 'chn','China', 63),
        (224, 'frg', 'West_Germany(_1989)', 109),
        (225, 'gdr','East_Germany(_1989)', 63),
        (127, 'ger','Germany', 109),
        (128, 'est','Estonia', 110),
        (129, 'esp','Spain', 111),
        (130, 'fin','Finland', 112),
        (131, 'fra','France', 113),
        (132, 'gre','Greece', 114),
        (133, 'irl','Ireland', 115),
        (134, 'ita','Italy', 116),
        (138, 'por','Portugal', 120),
        (145, 'pol','Poland', 127),
        (210, 'arg','Argentina', 186),
        (214, 'uru','Uruguay', 194),
        (137, 'ned','Nrtherlands', 119)
        ]
    
    c.executemany('INSERT INTO teams VALUES (?, ?, ?, ?)', data_to_insert)
    
    # Creando filas para events_teams
    data_to_insert = [
        (303, 17, 70),
        (64,5,224),
        (78,6,224),
        (93,7,224),
        (110,8,224),
        (127,9,224),
        (141,10,224),
        (158,11,224),
        (178,12,224),
        (203,13,224),
        (226,14,224),
        (142,10,225),
        (34,3,127),
        (21,2,127),
        (249,15,127),
        (282,16,127),
        (312,17,127),
        (334,18,127),
        (363,19,127),
        (414,20,127),
        (22,2,129),
        (47,4,129),
        (97,7,129),
        (115,8,129),
        (164,11,129),
        (185,12,129),
        (211,13,129),
        (233,14,129),
        (257,15,129),
        (288,16,129),
        (319,17,129),
        (340,18,129),
        (370,19,129),
        (420,20,129)]
    c.executemany('INSERT INTO events_teams VALUES (?, ?, ?)', data_to_insert)
    
     # Creando filas para games
     
    data_to_insert = [
        (1 , 1 , 'Matchday 1 ' ,131 ,190 , '1930-07-13 12:00', 4 , 1 , 1),
        (150, 7 , 'Matchday 2 ' ,223 ,129, '1962-05-31 12:00', 1 , 0 , 1),
        (151, 7 , 'Matchday 3 ' ,211 ,223, '1962-06-02 12:00', 0 , 0 , 0),
        (152, 7 , 'Matchday 4 ' ,129 ,190, '1962-06-03 12:00', 1 , 0 , 1),
        (153, 7 , 'Matchday 5 ' ,211 ,129, '1962-06-06 12:00', 2 , 1 , 1),
        (22 , 2 , 'Preliminary round ' ,129 ,211, '1934-05-27 12:00', 3 , 1 , 1),
        (31 , 2 , 'Quarter finals replays', 134 , 129 , '1934-06-01 12:00' , 1 , 0 , 1),
        (25 , 2 , 'Preliminary round ',134 ,191 , '1934-05-27 12:00' , 7 , 1 , 1),
        (32 , 2 , 'Semi-finals ' ,134 ,124, '1934-06-03 12:00' , 1 , 0 , 1),
        (35 , 2 , 'Final ' ,134 ,223, '1934-06-10 13:00' , 2 , 1 , 1),
        (40 , 3 , 'First round ' ,134 ,160, '1938-06-05 12:00' , 2 , 1 , 1),
        (752 ,19 , 'Matchday 6 ' ,129 ,153, '2010-06-16 16:00' , 0 , 1 , 2),
        (754 ,19 , 'Matchday 11 ' ,129 ,117, '2010-06-21 20:30' , 2 , 0 , 1),
        (755 ,19 , 'Matchday 15 ' ,212 ,129, '2010-06-25 20:30' , 1 , 2 , 2),
        (768 ,19 , 'Quarter finals ' ,213 ,129, '2010-07-03 20:30' , 0 , 1 , 2),
        (770 ,19 , 'Semifinals ' ,127 ,129, '2010-07-07 20:30' , 0 , 1 , 2),
        (772 ,19 , 'Final ' ,137 ,129, '2010-07-11 20:30' , 0 , 1 , 2)]
    
    c.executemany('INSERT INTO games VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', data_to_insert)