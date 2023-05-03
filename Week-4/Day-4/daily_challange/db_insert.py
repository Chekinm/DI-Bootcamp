from rest_countries import Country, get_info_for_countries, get_random_country_list_from_api
import psycopg2
from psycopg2 import sql

HOSTNAME = 'localhost'
USERNAME = 'psyco_user'
PASSWORD = 'psyco_user_password'
DATABASE = 'api_test'

def run_select_query (connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
     

def run_change_query (connection, query) -> bool: 
    """function runs change query, return True if change done 
    succesefully, otherwise return False"""
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except psycopg2.OperationalError as er:
        print(str(er))
        return False
    return True

def select_columns (table_name, *args):
    columns = ','.join(args) if args else '*'
    return  f'select {columns} from {table_name}'

def construct_query (country: Country) -> str:
    query = sql.SQL("""INSERT INTO from_api 
        (name, capital, flag_url, subregion, population)
        VALUES ({0},{1},{2},{3},{4})""").format(
        sql.Literal(country.name),
        sql.Literal(country.capital),
        sql.Literal(country.flag_url),
        sql.Literal(country.subregion),
        sql.Literal(country.population)
        )
        
    return query


try:
    connection = psycopg2.connect(
        host = HOSTNAME, 
        user = USERNAME, 
        password = PASSWORD, 
        dbname = DATABASE
        )
    
except psycopg2.OperationalError as er:
     connection = None
     print (er)

if connection:

    # number of countries to get from api and fetch into DB
    num = 200
    #request num rundom countries data from interntem
    count_from_api = get_random_country_list_from_api(num)

    countries_list = get_info_for_countries(count_from_api)

    for country in countries_list:
        query = construct_query(country)
        print(query)
        run_change_query(connection, query)



    print (*countries_list, sep='\n')



else:
    raise ConnectionError ('we have a problem with connection to database')











