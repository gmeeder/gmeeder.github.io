import snowflake.snowpark as snowpark
import snowflake.connector

def create_warehouse():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )
    
    # Obtener el cursor
    cursor = ctx.cursor()

    # Definir la consulta de creación de almacén
    create_warehouse_sql = '''
    CREATE WAREHOUSE EJEMPLO_WAREHOUSE
    WITH
    WAREHOUSE_SIZE=XSMALL
    MAX_CLUSTER_COUNT=3
    AUTO_SUSPEND = 300
    AUTO_RESUME = TRUE
    INITIALLY_SUSPENDED = TRUE
    COMMENT ="Ejemplo de warehouse"
    '''

    # Ejecutar la consulta de creación de almacén
    cursor.execute(create_warehouse_sql)

    # Crear Database para gestión de stages, fileformats, etc.
    create_database_sql = '''
    CREATE OR REPLACE DATABASE MANAGE_DB
    '''
    cursor.execute(create_database_sql)

    # Crear schema para stages externos
    create_schema_sql = '''
    CREATE OR REPLACE SCHEMA external_stages
    '''
    cursor.execute(create_schema_sql)

    # Crear external stage
    create_stage_sql = '''
    CREATE OR REPLACE STAGE MANAGE_DB.external_stages.aws_stage
        URL='s3://bucketsnowflakes3'
        CREDENTIALS=(AWS_KEY_ID='ABCD_DUMMY_ID' AWS_SECRET_KEY='1234abcd_key')
    '''
    cursor.execute(create_stage_sql)

    # Descripción del external stage
    describe_stage_sql = '''
    DESC STAGE MANAGE_DB.external_stages.aws_stage
    '''
    cursor.execute(describe_stage_sql)

    # Modificar external stage
    alter_stage_sql = '''
    ALTER STAGE aws_stage
        SET credentials=(AWS_KEY_ID='XYZ_DUMMY_ID' AWS_SECRET_KEY='987xyz')
    '''
    cursor.execute(alter_stage_sql)

    # Eliminar credenciales puesto que es un fichero público
    delete_credentials_sql = '''
    CREATE OR REPLACE STAGE MANAGE_DB.external_stages.aws_stage
        URL='s3://bucketsnowflakes3'
    '''
    cursor.execute(delete_credentials_sql)

    # Listar los ficheros en el stage
    list_files_sql = '''
    LIST @aws_stage
    '''
    cursor.execute(list_files_sql)

    # Cerrar el cursor
    cursor.close()
    
    # Confirmar la transacción
    ctx.commit()
    
    # Cerrar la conexión
    ctx.close()

# Para ejecutar la función directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    # Llamar a la función para crear el almacén y gestionar stages
    create_warehouse()
