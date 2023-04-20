import psycopg2
from psycopg2 import sql 
from dataclasses import dataclass



@dataclass
class MenuItem():
    # this data class represent menu item
    # this will be out type to store menu item if needed
    dish_name: str
    price: int
    def __str__(self):
        return (f'{self.dish_name.capitalize()}\t - {self.price} ils.')

class DBconnect():
    """ just connect to db"""
    def __init__(self, **db_env):
        try:
            self.connection = psycopg2.connect(**db_env)
            self.connection.autocommit = True

        except psycopg2.OperationalError as er:
            self.connection = None
            print (er) 


class DBSQLManager(DBconnect):
    """ database connection class, takes db_env data to connect
        it has  a connection attribute, 
        which is psycopg2 connection to database itself
        also has some methid to manage data from/to db"""
    
    def __init__(self, menu_name, **db_env):
        try:
            super().__init__(**db_env)
            self.table_id = sql.Identifier(menu_name)
            with self.connection.cursor() as cursor:
                cursor.execute(sql.SQL("""
                    CREATE TABLE IF NOT EXISTS {0} (
                    dish_id serial primary key,
                    dish_name varchar (30) NOT NULL,
                    price int NOT NULL)""").format(self.table_id)
                    )
                
        except psycopg2.OperationalError as er:
            self.connection = None
            print (er) 
        

    def get_by_name (self, dish_name) -> MenuItem:
        '''return menu item info from database as MenuItem
        return None if dish is not in db''' 
        with self.connection.cursor() as cursor:
            cursor.execute(sql.SQL("""
                SELECT
                    dish_name, price
                FROM
                    {}
                WHERE
                    dish_name = {}
                """).format(self.table_id, sql.Literal(dish_name)))
            result = cursor.fetchone()
        if result is None:
            return None # dish doesn't exist
        return MenuItem(result[0],result[1])
                
    def get_menu (self):
        ''' return all dishes from db in alphabetical order''' 
        with self.connection.cursor() as cursor:
            cursor.execute(sql.SQL("""
                SELECT
                    dish_name, price
                FROM
                    {}
                ORDER BY dish_name
                """).format(self.table_id))
            result = [MenuItem(item[0],item[1]) for item in cursor.fetchall()] 
            if result is None:
                return None # empty menu
            return result

    def add_dish (self, dish: MenuItem):
        '''insert new dish into DB''' 
        if not self.get_by_name(dish.dish_name):
            with self.connection.cursor() as cursor:
                cursor.execute(sql.SQL("""
                    INSERT INTO {} (dish_name, price)
                    VALUES ({}, {});
                    """).format(self.table_id, sql.Literal(dish.dish_name), sql.Literal(dish.price))) 
        else:
            raise ValueError (f'{dish.dish_name.capitalize()} already exist in database.')


    def update_dish (self, dish: MenuItem):
        '''insert new dish into DB''' 
        if self.get_by_name(dish.dish_name):
            with self.connection.cursor() as cursor:
                cursor.execute(sql.SQL("""
                    UPDATE {} SET price = {} WHERE dish_name = {};
                    """).format(self.table_id, sql.Literal(dish.price), sql.Literal(dish.dish_name))) 
        else:
            raise ValueError (f'{dish.dish_name.capitalize()} does not exist in database.')

    def delete_dish (self, dish: MenuItem):
        '''delete dish from DB''' 
        if self.get_by_name(dish.dish_name):
            with self.connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM menu_item WHERE dish_name = %s;
                    """, (dish.dish_name,)) 
        else:
            raise ValueError (f'{dish.dish_name.capitalize()} does not exist in database.')

        
    def display_tables_names (self):
        
        '''lookup for table names''' 
        with self.connection.cursor() as cursor:
            cursor.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'""")
            for table in cursor.fetchall():
                print(table)
            
        
        # if self.get_by_name(dish.dish_name):
        #     with self.connection.cursor() as cursor:
        #         cursor.execute("""
        #             DELETE FROM menu_item WHERE dish_name = %s;
        #             """, (dish.dish_name,)) 
        # else:
        #     raise ValueError (f'{dish.dish_name.capitalize()} does not exist in database.')

    

    def self_delete(self):
        """carefull with this.
         it deletes instance db_table connected to menu_item instance,
          and clse connecton to database,
         but looks like don't delete the instance itself
         should refactor this in some way, need more googling"""

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql.SQL("""
                    DROP TABLE IF EXISTS {0}""").format(self.table_id)
                    )
            self.connection.close()
         
                
        except psycopg2.OperationalError as er:
            self.connection = None
            print (er) 
        


# from menumanager import MenuItem, DBSQLManager

# db_env = {
#     'host': 'localhost',
#     'user': 'psyco_user',
#     'password': 'psyco_user_password',
#     'dbname': 'menu_manager',
# }

# menu_name = 'menu_item1'
# db = DBSQLManager(menu_name, **db_env)
# print('aaaaaaaa', db)
# #print(db.get_by_name('burger'))
# #print(*db.get_menu(), sep='\n')
# pasta = MenuItem('pasta',140)
# #db.add_dish(pasta)

# burger = MenuItem('burger', 400)
# db.update_dish(burger)

# #db.delete_dish(pasta)
# print(*db.get_menu(), sep='\n')

