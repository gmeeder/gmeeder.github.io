import snowflake.snowpark as snowpark
import snowflake.connector

def manage_pipe():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )

    # Iniciar la sesión
    session = snowpark.Session.builder().build()

    # Descripción del pipe
    describe_pipe_sql = '''
    DESC PIPE MANAGE_DB.pipes.employee_pipe
    '''
    result = session.execute(describe_pipe_sql)

    # Imprimir la descripción del pipe
    for row in result:
        print(row)

    # Mostrar todos los pipes
    show_pipes_sql = '''
    SHOW PIPES
    '''
    result = session.execute(show_pipes_sql)

    # Imprimir todos los pipes
    for row in result:
        print(row)

    # Mostrar pipes que contienen 'employee' en su nombre
    show_pipes_like_sql = '''
    SHOW PIPES LIKE '%employee%'
    '''
    result = session.execute(show_pipes_like_sql)

    # Imprimir pipes que contienen 'employee' en su nombre
    for row in result:
        print(row)

    # Mostrar pipes en el database MANAGE_DB
    show_pipes_in_db_sql = '''
    SHOW PIPES IN DATABASE MANAGE_DB
    '''
    result = session.execute(show_pipes_in_db_sql)

    # Imprimir pipes en el database MANAGE_DB
    for row in result:
        print(row)

    # Mostrar pipes en el schema MANAGE_DB.pipes
    show_pipes_in_schema_sql = '''
    SHOW PIPES IN SCHEMA MANAGE_DB.pipes
    '''
    result = session.execute(show_pipes_in_schema_sql)

    # Imprimir pipes en el schema MANAGE_DB.pipes
    for row in result:
        print(row)

    # Mostrar pipes que contienen 'employee' en su nombre en el database MANAGE_DB
    show_pipes_like_in_db_sql = '''
    SHOW PIPES LIKE '%employee%' IN DATABASE MANAGE_DB
    '''
    result = session.execute(show_pipes_like_in_db_sql)

    # Imprimir pipes que contienen 'employee' en su nombre en el database MANAGE_DB
    for row in result:
        print(row)

    # Pausar el pipe
    alter_pipe_pause_sql = '''
    ALTER PIPE MANAGE_DB.pipes.employee_pipe SET PIPE_EXECUTION_PAUSED = TRUE
    '''
    session.execute(alter_pipe_pause_sql)

    # Verificar el estado del pipe pausado
    verify_pipe_status_sql = '''
    SELECT SYSTEM$PIPE_STATUS('MANAGE_DB.pipes.employee_pipe')
    '''
    result = session.execute(verify_pipe_status_sql)

    # Imprimir el estado del pipe pausado
    for row in result:
        print(row)

    # Recrear el pipe y cambiar la definición en el COPY
    recreate_pipe_sql = '''
    CREATE OR REPLACE PIPE MANAGE_DB.pipes.employee_pipe
    AUTO_INGEST = TRUE
    AS
    COPY INTO PRIMERABBDD.PRIMERESQUEMA.employees2
    FROM @MANAGE_DB.external_stages.csv_folder  
    '''
    session.execute(recreate_pipe_sql)

    # Refrescar el pipe alterado
    alter_pipe_refresh_sql = '''
    ALTER PIPE MANAGE_DB.pipes.employee_pipe REFRESH
    '''
    session.execute(alter_pipe_refresh_sql)

    # Listar archivos en el stage
    list_files_sql = '''
    LIST @MANAGE_DB.external_stages.csv_folder  
    '''
    result = session.execute(list_files_sql)

    # Imprimir la lista de archivos en el stage
    for row in result:
        print(row)

    # Seleccionar datos de la tabla
    select_data_sql = '''
    SELECT * FROM PRIMERABBDD.PRIMERESQUEMA.employees2
    '''
    result = session.execute(select_data_sql)

    # Imprimir los datos de la tabla
    for row in result:
        print(row)

    # Recargar manualmente los archivos que estaban en el bucket previamente
    copy_into_sql = '''
    COPY INTO PRIMERABBDD.PRIMERESQUEMA.employees2
    FROM @MANAGE_DB.external_stages.csv_folder  
    '''
    session.execute(copy_into_sql)

    # Reactivar el pipe
    alter_pipe_resume_sql = '''
    ALTER PIPE MANAGE_DB.pipes.employee_pipe SET PIPE_EXECUTION_PAUSED = FALSE
    '''
    session.execute(alter_pipe_resume_sql)

    # Verificar el estado del pipe activo de nuevo
    verify_pipe_status_again_sql = '''
    SELECT SYSTEM$PIPE_STATUS('MANAGE_DB.pipes.employee_pipe')
    '''
    result = session.execute(verify_pipe_status_again_sql)

    # Imprimir el estado del pipe activo de nuevo
    for row in result:
        print(row)

    # Cerrar la conexión
    ctx.close()

# Para ejecutar la función directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    # Ejecutar las consultas de gestión del pipe
    manage_pipe()
