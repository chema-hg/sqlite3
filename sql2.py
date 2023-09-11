import sqlite3

# Creamos la conexion
with sqlite3.connect('base.db') as conexion:
    # Creamos el cursor
    cursor = conexion.cursor()
    # Enumera el nombre de todos los equipos que han participado alguna vez
    # en el mundial.
    # CONSULTA SQL
    CONSULTA = """
    SELECT t.title
    FROM teams AS t
    INNER JOIN events_teams AS et ON et.team_id = t.id
    INNER JOIN events AS e ON e.id = et.event_id;
    """
#     SELECT t.title: Esta parte de la CONSULTA indica que queremos seleccionar la columna title de la tabla teams (alias t).
#     En otras palabras, estamos extrayendo solamente los títulos de los equipos.
    
#     FROM teams AS t: Establece la fuente de datos para la CONSULTA. Estamos seleccionando datos de la tabla teams y la estamos
#     apodando como t para simplificar la escritura de la CONSULTA.

# INNER JOIN events_teams AS et ON et.team_id = t.id: Esta parte de la CONSULTA realiza una operación de JOIN (unión)
# entre dos tablas:
# teams (alias t) y events_teams (alias et). Estamos uniendo estas dos tablas en función de que el campo team_id
# en la tabla events_teams coincida con el campo id en la tabla teams. Esta operación permite combinar información de ambas
# tablas basándose en una relación entre ellas.

# INNER JOIN events AS e ON e.id = et.event_id: Continuamos realizando otra operación de JOIN, esta vez uniendo la tabla events
# (alias e) con la tabla events_teams (alias et). Estamos relacionando estas dos tablas mediante los campos id en la tabla events
# y event_id en la tabla events_teams.

    # Ejecutar la CONSULTA
    cursor.execute(CONSULTA)

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Procesar los resultados (en este ejemplo, solo imprimirlos)
    print('Nombre de todos los equipos que han participado alguna vez en el mundial:')
    for fila in resultados:
        print(fila)
        
    # Muestra la fecha de inicio de todas las ediciones del mundial.
    CONSULTA = """
    SELECT events.[key],
    events.start_at
    FROM events;"""
    
#     SELECT events.[key], events.start_at: Esta parte de la CONSULTA especifica las columnas que quieres seleccionar en el resultado.
#     En este caso, estás seleccionando dos columnas: [key] y start_at de la tabla events. El uso de corchetes [key] sugiere que
#     el nombre de la columna contiene caracteres especiales o espacios, por lo que se usa entre corchetes para evitar ambigüedades.
    
    cursor.execute(CONSULTA)
    resultados = cursor.fetchall()
    print('Fecha de inicio de todas las ediciones del mundial:')
    for fila in resultados:
        print(f"Mundial: {fila[0]} - Fecha inicio: {fila[1]}")
        
    # Para un mundial muestra en dos columnas para cada partido el nombre
    # de los dos paises que se enfrentaron entre si.
    CONSULTA =CONSULTA = """
    SELECT t1.title, t2.title
    FROM games AS g
    INNER JOIN teams AS t1 ON t1.id = g.team1_id
    INNER JOIN teams AS t2 ON t2.id = g.team2_id
    INNER JOIN events AS e ON e.id = g.event_id
    WHERE e.[key] = 'world.2010';
    """
    cursor.execute(CONSULTA)
    resultados = cursor.fetchall()
    print('Para un mundial el nombre de los dos paises que se enfrentaron entre si:')
    for fila in resultados:
        print(fila)
        
    # A la CONSULTA anterior añade además la puntuación final de cada uno de
    # los dos equipos.
    CONSULTA = """
    SELECT t1.title, g.score1, g.score2, t2.title
    FROM games AS g
    INNER JOIN teams AS t1 ON t1.id = g.team1_id
    INNER JOIN teams AS t2 ON t2.id = g.team2_id
    INNER JOIN events AS e ON e.id = g.event_id
    WHERE e.[key] = 'world.2010';
    """
    cursor.execute(CONSULTA)
    resultados = cursor.fetchall()
    print('Paises que se enfrentaron entre si y resultado:')
    for fila in resultados:
        print(fila)
        
#     Muestra el nombre de los equipos que participaron en la primera edición
#     de la que tenemos datos.

    CONSULTA = """
    SELECT t.title
    FROM teams AS t
    INNER JOIN events_teams AS et ON et.team_id = t.id
    INNER JOIN events AS e ON e.id = et.event_id
    WHERE e.id = 2;
    """
    cursor.execute(CONSULTA)
    resultados = cursor.fetchall()
    print('\n5. Equipos de la primera edición que tenemos datos:')
    for fila in resultados:
        print(fila)

# 6. Lista los partidos que se hayan realizado entre el 1900
# y el 2010 en los que haya habido al menos un gol.
    CONSULTA = """
    SELECT e.[key] AS EdicionCopa,
           e.start_at AS FechaPartido,
           t1.title,
           g.score1,
           g.score2,
           t2.title
    FROM games AS g
    INNER JOIN teams AS t1 ON t1.id = g.team1_id
    INNER JOIN teams AS t2 ON t2.id = g.team2_id
    INNER JOIN events AS e ON e.id = g.event_id
    WHERE (e.start_at BETWEEN '1900-01-01' AND '2010-01-01')
          AND (g.score2 > 0 OR g.score1 > 0);
    """
    cursor.execute(CONSULTA)
    resultados = cursor.fetchall()
    print('\n6.- Partidos entre 1900 y 2010 en los que ha habido al menos un gol:')
    for fila in resultados:
        print(fila)
        
#     muestra en que ediciones del mundial ha estado la selección española.
    CONSULTA = """
    SELECT DISTINCT e.[key]
    FROM events_teams AS et,
     events AS e
    INNER JOIN
     teams AS t1 ON t1.title = 'Spain'
    WHERE t1.id = et.team_id;
    """
#     busca obtener las claves únicas de eventos (e.[key]) donde el equipo con el título 'Spain' (t1.title = 'Spain')
#     estuvo involucrado. Esta CONSULTA implica una combinación de las tablas events_teams (con alias et), events (con alias e),
#     y teams (con alias t1) a través de operaciones de JOIN. La CONSULTA utiliza DISTINCT para asegurarse de que solo se
#     devuelvan valores de clave únicos   
    cursor.execute(CONSULTA)
    resultados = cursor.fetchall()
    print('\n7.- ediciones del mundial ha estado la selección española:')
    for fila in resultados:
        print(fila)
    