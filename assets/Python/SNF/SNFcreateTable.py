#pto GAC telsur 

"""
Con el fin mejorar el rendimiento de los tableros de control presupuestario para los segmentos residencial y Pyme, se plantea el paso de los archivos normalizados
a presupuesto la nube corporativa SNF, para esto se desarrolla siguiente propuestas de codigo python para la creacion de la tabla e insercion de contenido 
"""
# Al no conocer la db y esquema de destino, solo se plantea la creacion e insercion

#--
#CREACION TABLA PresupuestoAltas
#--
import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import snowflake.connector

def main(session: snowpark.Session):
    # Obtener el cursor
    cursor = session.connection.cursor()

    # Definir la consulta de creación de tabla
    create_table_sql = '''
    CREATE OR REPLACE TABLE PresupuestoAltas (
        Nombre STRING,
        Descripcion STRING,
        Zonal_pto STRING,
        Fecha_pto DATE,
        Cate_cliente_Pto STRING,
        Cate_cliente_Pto2 STRING,
        Q_pto INTEGER,
        MOvalor_pto STRING,
        tipoServicio_pto STRING,
        tipo_actividad STRING,
        TIPO_PETICION STRING
    )
    '''

    # Ejecutar la consulta de creación de tabla
    cursor.execute(create_table_sql)

    # Insertar datos en la tabla
    insert_sql = '''
    INSERT INTO PresupuestoAltas VALUES
    ('', '', '', '', , '', '', '', '')
    '''

    # Ejecutar la inserción de datos
    cursor.execute(insert_sql)

    # Confirmar la transacción
    cursor.execute("COMMIT")

    # Cerrar el cursor
    cursor.close()

# Para ejecutar la función main directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    session = snowpark.Session.builder().build()
    # Configurar la codificación de salida a UTF-8
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    main(session)
    print("Tabla 'PresupuestoAltas' creada correctamente.")

#--
#CREACION TABLA PresupuestoReparaciones
#--

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import snowflake.connector

def main(session: snowpark.Session):
    # Obtener el cursor
    cursor = session.connection.cursor()

    # Definir la consulta de creación de tabla
    create_table_sql = '''
    CREATE OR REPLACE TABLE PresupuestoReparaciones (
        Nombre STRING,
        Descripcion STRING,
        Zonal_pto STRING,
        Fecha_pto DATE,
        Cate_cliente_Pto STRING,
        Cate_cliente_Pto2 STRING,
        Q_pto INTEGER,
        MOvalor_pto STRING,
        tipoServicio_pto STRING,
        tipo_actividad STRING,
        TIPO_PETICION STRING
    )
    '''

    # Ejecutar la consulta de creación de tabla
    cursor.execute(create_table_sql)

    # Insertar datos en la tabla
    insert_sql = '''
    INSERT INTO PresupuestoAltas VALUES
    ('', '', '', '', , '', '', '', '')
    '''

    # Ejecutar la inserción de datos
    cursor.execute(insert_sql)

    # Confirmar la transacción
    cursor.execute("COMMIT")

    # Cerrar el cursor
    cursor.close()

# Para ejecutar la función main directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    session = snowpark.Session.builder().build()
    # Configurar la codificación de salida a UTF-8
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    main(session)
    print("Tabla 'PresupuestoAltas' creada correctamente.")


#//
#INSERTAR datos TABLA PresupuestoAltas y PresupuestoReparaciones
#//


import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import snowflake.connector

def insert_data(session: snowpark.Session):
    # Obtener el cursor
    cursor = session.connection.cursor()

    # Definir los datos a insertar
    data_to_insert = [
        ('', '', '', '', '', '', , '', '', '', ''),
        ('', '', '', '', '', '', , '', '', '', '')
    ]

    # Definir la consulta de inserción
    insert_sql = '''
    INSERT INTO PresupuestoAltas (Nombre, Descripcion, Zonal_pto, Fecha_pto, Cate_cliente_Pto, Cate_cliente_Pto2, Q_pto, MOvalor_pto, tipoServicio_pto, tipo_actividad, TIPO_PETICION)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # Ejecutar la consulta de inserción para cada conjunto de datos
    for row in data_to_insert:
        cursor.execute(insert_sql, row)

    # Confirmar la transacción
    cursor.execute("COMMIT")

    # Cerrar el cursor
    cursor.close()

# Para ejecutar la función insert_data directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    session = snowpark.Session.builder().build()
    # Configurar la codificación de salida a UTF-8
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    insert_data(session)
    print("Datos insertados correctamente en la tabla 'PresupuestoAltas'.")

#--
#CREACION TABLA PresupuestoModificaciones
#--

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import snowflake.connector

def main(session: snowpark.Session):
    # Obtener el cursor
    cursor = session.connection.cursor()

    # Definir la consulta de creación de tabla
    create_table_sql = '''
    CREATE OR REPLACE TABLE PresupuestoModificaciones (
        Zonal STRING,
        Fecha DATE,
        Tipo_trabajo STRING,
        Tipo_servicio STRING,
        Q_pto INTEGER,
        Monto_pto STRING,
        Cate_cliente_Pto STRING,
        Cate_cliente_Pto2 STRING
    )
    '''

    # Ejecutar la consulta de creación de tabla
    cursor.execute(create_table_sql)

    # Insertar datos en la tabla
    insert_sql = '''
    INSERT INTO PresupuestoModificaciones VALUES
    ('', '', '', '', , '', '', '')
    '''

    # Ejecutar la inserción de datos
    cursor.execute(insert_sql)

    # Confirmar la transacción
    cursor.execute("COMMIT")

    # Cerrar el cursor
    cursor.close()

# Para ejecutar la función main directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    session = snowpark.Session.builder().build()
    # Configurar la codificación de salida a UTF-8
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    main(session)
    print("Tabla 'PresupuestoModificaciones' creada correctamente.")



#//
#INSERTAR datos TABLA PresupuestoModificaciones
#//

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import snowflake.connector

def insert_data(session: snowpark.Session):
    # Obtener el cursor
    cursor = session.connection.cursor()

    # Definir los datos a insertar
    data_to_insert = [
        ('', '', '', '', , '', '', ''),
        ('', '', '', '', , '', '', '')
        # Puedes agregar más filas de datos aquí si es necesario
    ]

    # Definir la consulta de inserción
    insert_sql = '''
    INSERT INTO PresupuestoModificaciones (Zonal, Fecha, Tipo_trabajo, Tipo_servicio, Q_pto, Monto_pto, Cate_cliente_Pto, Cate_cliente_Pto2)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # Ejecutar la consulta de inserción para cada conjunto de datos
    for row in data_to_insert:
        cursor.execute(insert_sql, row)

    # Confirmar la transacción
    cursor.execute("COMMIT")

    # Cerrar el cursor
    cursor.close()

# Para ejecutar la función insert_data directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    session = snowpark.Session.builder().build()
    # Configurar la codificación de salida a UTF-8
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    insert_data(session)
    print("Datos insertados correctamente en la tabla 'PresupuestoModificaciones'.")




#--
#CREACION e INSERCION datos TABLA PresupuestoTraslados
#--

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import snowflake.connector

def main(session: snowpark.Session):
    # Obtener el cursor
    cursor = session.connection.cursor()

    # Definir la consulta de creación de tabla
    create_table_sql = '''
    CREATE OR REPLACE TABLE PresupuestoTraslados (
        Zonal STRING,
        Fecha DATE,
        Tipo_trabajo STRING,
        Tipo_peticion STRING,
        Clas_peticion STRING,
        Tipo_servicio STRING,
        Q_pto INTEGER,
        Monto_pto STRING,
        Cate_cliente_Pto STRING,
        Cate_cliente_Pto2 STRING
    )
    '''

    # Ejecutar la consulta de creación de tabla
    cursor.execute(create_table_sql)

    # Insertar datos en la tabla
    insert_sql = '''
    INSERT INTO PresupuestoTraslados VALUES
    ('', '', '', '', '', '', , '', '', '')
    '''

    # Ejecutar la inserción de datos
    cursor.execute(insert_sql)

    # Confirmar la transacción
    cursor.execute("COMMIT")

    # Cerrar el cursor
    cursor.close()

# Para ejecutar la función main directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    session = snowpark.Session.builder().build()
    # Configurar la codificación de salida a UTF-8
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    main(session)
    print("Tabla 'PresupuestoTraslados' creada correctamente.")






[Tipo Material]
CABLE FO DROP
CONECTOR DE CAMPO
EQUIPO ONT - Fiber Home
EQUIPO ONT- Zhone

EQUIPO ONT_3Modelos
if [Tipo Material] == 'CABLE FO DROP' then 'CABLE FO DROP'
elseif [Tipo Material] == 'CONECTOR DE CAMPO' then 'CONECTOR DE CAMPO'
elseif [Tipo Material] == 'EQUIPO ONT - Fiber Home'
or [Tipo Material] == 'EQUIPO ONT- Zhone' then 'EQUIPO ONT'
else 'Gestion Operativa'
end 








Visualizacion Route Date (copia)

if  [Route Date.p] ='Día' then DATETRUNC('day', [RouteDate])
elseif  [Route Date.p] ='Semana' then DATETRUNC('week', [RouteDate])
elseif  [Route Date.p] ='Mes' then DATETRUNC('month', [RouteDate])
end
























