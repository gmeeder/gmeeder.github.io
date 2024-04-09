import snowflake.snowpark as snowpark
import snowflake.connector

def create_share_and_permissions():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )

    # Iniciar la sesión
    session = snowpark.Session.builder().build()

    # Crear objeto share
    create_share_sql = '''
    CREATE OR REPLACE SHARE ORDERS_SHARE
    '''
    session.execute(create_share_sql)

    # Dar permisos a la base de datos
    grant_usage_on_db_sql = '''
    GRANT USAGE ON DATABASE PRIMERABBDD TO SHARE ORDERS_SHARE
    '''
    session.execute(grant_usage_on_db_sql)

    # Dar permisos al esquema
    grant_usage_on_schema_sql = '''
    GRANT USAGE ON SCHEMA PRIMERABBDD.PRIMERESQUEMA TO SHARE ORDERS_SHARE
    '''
    session.execute(grant_usage_on_schema_sql)

    # Dar permisos a la tabla
    grant_select_on_table_sql = '''
    GRANT SELECT ON TABLE PRIMERABBDD.PRIMERESQUEMA.ORDERS TO SHARE ORDERS_SHARE
    '''
    session.execute(grant_select_on_table_sql)

    # Verificar permisos
    show_grants_sql = '''
    SHOW GRANTS TO SHARE ORDERS_SHARE
    '''
    result = session.execute(show_grants_sql)

    # Imprimir los permisos
    for row in result:
        print(row)

    # Cerrar la conexión
    ctx.close()

def add_consumer_account_to_share():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )

    # Iniciar la sesión
    session = snowpark.Session.builder().build()

    # Añadir la cuenta del consumidor al share
    add_account_to_share_sql = '''
    ALTER SHARE ORDERS_SHARE ADD ACCOUNT = <cuenta_consumidor>
    '''
    session.execute(add_account_to_share_sql)

    # Cerrar la conexión
    ctx.close()

def consume_shared_data():
    # Establecer la conexión
    ctx = snowflake.connector.connect(
        user='<TU_USUARIO>',
        password='<TU_CONTRASEÑA>',
        account='<TU_CUENTA>'
    )

    # Iniciar la sesión
    session = snowpark.Session.builder().build()

    # Ver las comparticiones con el usuario
    show_shares_sql = '''
    SHOW SHARES
    '''
    result = session.execute(show_shares_sql)

    # Imprimir las comparticiones
    for row in result:
        print(row)

    # Detalle del share
    describe_share_sql = '''
    DESC SHARE ORDERS_SHARE
    '''
    result = session.execute(describe_share_sql)

    # Imprimir el detalle del share
    for row in result:
        print(row)

    # Crear base de datos en la cuenta consumidora usando el share
    create_database_sql = '''
    CREATE DATABASE PRIMERABBDD FROM SHARE ORDERS_SHARE
    '''
    session.execute(create_database_sql)

    # Validar resultados
    select_data_sql = '''
    SELECT * FROM PRIMERABBDD.PRIMERESQUEMA.ORDERS
    '''
    result = session.execute(select_data_sql)

    # Imprimir los resultados
    for row in result:
        print(row)

    # Cerrar la conexión
    ctx.close()

# Para ejecutar la función directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    # Crear share y permisos
    create_share_and_permissions()

    # Añadir la cuenta del consumidor al share
    add_consumer_account_to_share()

    # Consumir los datos compartidos
    consume_shared_data()
