import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'psyco_user'
PASSWORD = 'psyco_user_password'
DATABASE = 'psyco_test'

try:
    connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)
except psycopg2.OperationalError as er:
     connection = None
     print (er)

def run_select_query (connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        a = cursor.fetchone()
        yield a
     

def run_change_query (connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
    return result

def select_columns (table_name, *args):
    columns = ','.join(args) if args else '*'
    return  f'select {columns} from {table_name}'


query = select_columns('test', 'user_name', 'user_age')
if connection:
    print(run_select_query(connection, query))
    # with connection.cursor() as cursor:
    #     cursor.execute(query)
    #     print(type(cursor.fetchone()))
    #     #print(a)
    #     # a = cursor.fetchone()
    #     # print(a)
else:
    raise ConnectionError ('we have a problem with connection to database')
