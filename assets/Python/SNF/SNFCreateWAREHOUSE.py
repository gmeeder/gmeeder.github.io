
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

    # Confirmar la transacción
    cursor.execute("COMMIT")

    # Cerrar el cursor
    cursor.close()
    
    # Cerrar la conexión
    ctx.close()

# Para ejecutar la función directamente si este script es ejecutado como un programa independiente
if __name__ == "__main__":
    # Llamar a la función para crear el almacén
    create_warehouse()
