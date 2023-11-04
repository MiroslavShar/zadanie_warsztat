import psycopg2
from psycopg2.errors import DuplicateDatabase, DuplicateTable, OperationalError

def create_db(cursor):
    query = """
            CREATE DATABASE users_app;
            """
    try:
        cursor.execute(query)
        cursor.close()

    except psycopg2.DuplicateDatabase as error:
        print("Baza danych istnieje: ", error)

def create_table_users(cursor):
    try:
        query = """
        CREATE TABLE users 
        (
        id serial Primary key, 
        username varchar(155), 
        hashed_password varchar(80)
        ); 
        """
        cursor.execute(query)
        cursor.close()
    except psycopg2.ProgrammingError as error:
        print("Tabela istnieje: ", error)

def create_table_messages(errors, cursor):
    text = errors
    query = """
    CREATE TABLE messages
    (
    id serial Primary key,
    from_id int,
    to_id int,
    creation_date timestamp,
    text varchar(255),
    FOREIGN KEY (from_id) REFERENCES users,
    FOREIGN KEY (to_id) REFERENCES users
    )
    """
    try:
        cursor.execute(query)
        cursor.close()
    except psycopg2.DuplicateTable as error:
        print("Tabela istnieje: ", error)


