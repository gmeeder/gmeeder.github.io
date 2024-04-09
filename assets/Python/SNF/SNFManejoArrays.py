import snowflake.snowpark as snowpark
import snowflake.connector

def run_queries():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )

    # Iniciar la sesión
    session = snowpark.Session.builder().build()

    # Ejecutar la primera consulta
    query1 = '''
    SELECT
        RAW_FILE:prev_company as prev_company
    FROM PRIMERABBDD.PRIMERESQUEMA.JSON_RAW
    '''
    result1 = session.execute(query1)

    # Imprimir los resultados de la primera consulta
    for row in result1:
        print(row["PREV_COMPANY"])

    # Ejecutar la segunda consulta
    query2 = '''
    SELECT
        RAW_FILE:prev_company[1]::STRING as prev_company
    FROM PRIMERABBDD.PRIMERESQUEMA.JSON_RAW
    '''
    result2 = session.execute(query2)

    # Imprimir los resultados de la segunda consulta
    for row in result2:
        print(row["PREV_COMPANY"])

    # Ejecutar la tercera consulta
    query3 = '''
    SELECT
        ARRAY_SIZE(RAW_FILE:prev_company) as prev_company
    FROM PRIMERABBDD.PRIMERESQUEMA.JSON_RAW
    '''
    result3 = session.execute(query3)

    # Imprimir los resultados de la tercera consulta
    for row in result3:
        print(row["PREV_COMPANY"])

    # Cerrar la conexión
    ctx.close()

# Para ejecutar la función directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    # Ejecutar las consultas
    run_queries()
