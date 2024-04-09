import snowflake.snowpark as snowpark
import snowflake.connector

def create_pipe_and_describe():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )

    # Iniciar la sesión
    session = snowpark.Session.builder().build()

    # Definir el pipe
    create_pipe_sql = '''
    CREATE OR REPLACE PIPE MANAGE_DB.pipes.employee_pipe
    AUTO_INGEST = TRUE
    AS
    COPY INTO PRIMERABBDD.PRIMERESQUEMA.employees
    FROM @MANAGE_DB.external_stages.csv_folder  
    '''
    session.execute(create_pipe_sql)

    # Descripción del pipe
    describe_pipe_sql = '''
    DESC PIPE employee_pipe
    '''
    result = session.execute(describe_pipe_sql)

    # Imprimir la descripción del pipe
    for row in result:
        print(row)

    # Mostrar datos de la tabla de destino
    select_data_sql = '''
    SELECT * FROM PRIMERABBDD.PRIMERESQUEMA.employees 
    '''
    result = session.execute(select_data_sql)

    # Imprimir los datos de la tabla de destino
    for row in result:
        print(row)

    # Cerrar la conexión
    ctx.close()

# Para ejecutar la función directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    # Ejecutar la creación del pipe y descripción
    create_pipe_and_describe()
