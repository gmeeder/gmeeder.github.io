import snowflake.snowpark as snowpark
import snowflake.connector

def create_schema_and_stages():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )
    
    # Obtener el cursor
    cursor = ctx.cursor()

    # Crear esquema
    create_schema_sql = '''
    CREATE OR REPLACE SCHEMA MANAGE_DB.INTERNAL_STAGES
    '''
    cursor.execute(create_schema_sql)

    # Crear internal stage
    create_internal_stage_sql = '''
    CREATE OR REPLACE STAGE MANAGE_DB.INTERNAL_STAGES.JSONSTAGE
    '''
    cursor.execute(create_internal_stage_sql)

    # Crear external stage
    create_external_stage_sql = '''
    CREATE OR REPLACE STAGE MANAGE_DB.EXTERNAL_STAGES.JSONSTAGE
         URL='s3://bucketsnowflake-jsondemo'
    '''
    cursor.execute(create_external_stage_sql)

    # Definir el formato tipo JSON
    create_json_format_sql = '''
    CREATE OR REPLACE FILE FORMAT MANAGE_DB.FILE_FORMATS.JSONFORMAT
        TYPE = JSON
    '''
    cursor.execute(create_json_format_sql)

    # Crear tabla para datos JSON_RAW
    create_table_sql = '''
    CREATE OR REPLACE TABLE PRIMERABBDD.PRIMERESQUEMA.JSON_RAW (
        raw_file VARIANT
    )
    '''
    cursor.execute(create_table_sql)

    # Copiar datos en la tabla JSON_RAW desde el internal stage
    copy_into_sql = '''
    COPY INTO PRIMERABBDD.PRIMERESQUEMA.JSON_RAW
        FROM @MANAGE_DB.INTERNAL_STAGES.JSONSTAGE
        FILE_FORMAT=MANAGE_DB.FILE_FORMATS.JSONFORMAT
        FILES=('HR_data.json')
    '''
    cursor.execute(copy_into_sql)

    # Mostrar los datos de la tabla JSON_RAW
    select_data_sql = '''
    SELECT * FROM PRIMERABBDD.PRIMERESQUEMA.JSON_RAW
    '''
    cursor.execute(select_data_sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Cerrar el cursor
    cursor.close()
    
    # Confirmar la transacción
    ctx.commit()
    
    # Cerrar la conexión
    ctx.close()

# Para ejecutar la función directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    # Llamar a la función para crear el esquema y los stages
    create_schema_and_stages()
