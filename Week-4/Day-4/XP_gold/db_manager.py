import psycopg2

    
DB_CONFIG = {'host': 'localhost',
            'user': 'psyco_user',
            'password': 'psyco_user_password',
            'dbname': 'menu_manager',
            }


class DBconnect():
    """class to work with database"""
    """instance of class is a database, with connection as property"""

    def __init__(self, **DB_CONFIG):
        print(DB_CONFIG)
        """create an instance of connection to the database
        will be none if there some poblem with DB"""
        try:
            self.connection = psycopg2.connect(**DB_CONFIG)
            self.connection.autocommit = True
            with self.connection.cursor() as cursor:
                cursor.execute(open('./tables_create.sql', 'r').read())
                print('db_Created')
        
        except psycopg2.OperationalError as error:
            self.connection = None
            print (error)



    def _run_change_query (self, query) -> bool: 
        """function runs change query, return True if change done 
        succesefully, otherwise return False
        inside it check if id already exist and update existing record with new values"""
       
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                # self.commit()
        except psycopg2.OperationalError as er:
            print(str(er))
            return False
        return True
    

    def add_user (self, username:str, password:str) -> bool: 
        """function create user with default values"""
        query = f"INSERT INTO user_password (username, password) VALUES('{username}','{password}') ON CONFLICT (username) DO NOTHING;" 
        return self._run_change_query(query)
    

    def delete_user (self, username:str) -> bool: 
        """delete user from db"""
        query = f"DELETE FROM user_password WHERE username='{username}'" 
        return self._run_change_query(query)

    def get_user (self, username:str)-> bool:
        """check if user exist in database"""
        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT username, password FROM  user_password WHERE username='{username}'" 
                cursor.execute(query)
                res = cursor.fetchall()
                print(res)
                return res[0] if res else []
        except psycopg2.OperationalError as er:
            print(str(er))
            return []

    def change_password (self, username:str, password:str)->bool:
        """function update users password """
        query = f"UPDATE user_password SET password={password}  WHERE username = '{username}'" 
        return self._run_change_query(query)
    

