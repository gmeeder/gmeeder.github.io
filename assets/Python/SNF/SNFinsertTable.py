
# Al no conocer la db y esquema de destino, solo se plantea la creacion e insercion


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

