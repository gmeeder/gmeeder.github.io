import snowflake.snowpark as snowpark
import snowflake.connector

def create_integration_and_describe():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )

    # Iniciar la sesión
    session = snowpark.Session.builder().build()

    # Crear objeto de integración de almacenamiento
    create_integration_sql = '''
    CREATE OR REPLACE STORAGE INTEGRATION s3_int
        TYPE = EXTERNAL_STAGE
        STORAGE_PROVIDER = S3
        ENABLED = TRUE 
        STORAGE_AWS_ROLE_ARN = ''
        STORAGE_ALLOWED_LOCATIONS = ('s3://<tu-nombre-de-bucket>/<tu-ruta>/', 's3://<tu-nombre-de-bucket>/<tu-ruta>/')
        COMMENT = 'Comentario opcional'
    '''
    session.execute(create_integration_sql)

    # Verificar propiedades del objeto de integración
    describe_integration_sql = '''
    DESC INTEGRATION s3_int
    '''
    result = session.execute(describe_integration_sql)

    # Imprimir los resultados de la descripción del objeto de integración
    for row in result:
        print(row)

    # Cerrar la conexión
    ctx.close()

# Para ejecutar la función directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    # Ejecutar la creación del objeto de integración y la descripción
    create_integration_and_describe()
