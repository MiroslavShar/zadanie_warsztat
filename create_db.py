import psycopg2
from psycopg2.errors import DuplicateDatabase, DuplicateTable, OperationalError
from psycopg2 import errors

def create_db(cursor):
    try:
        query = """
            CREATE DATABASE users_app;
            """
        cursor.execute(query)
    except errors.DuplicateDatabase:
        print("The database exists")

def create_table_users(cursor_second):
    try:
        query = """
        CREATE TABLE users 
        (
        id serial Primary key, 
        username varchar(155), 
        hashed_password varchar(80)
        ); 
        """
        cursor_second.execute(query)
    except errors.DuplicateTable:
        print("The Table exists")

def create_table_messages(cursor_second):
    text = errors
    query = """
    CREATE TABLE messages
    (
    id serial Primary key,
    from_id int,
    to_id int,
    creation_date timestamp,
    text varchar(255),
    FOREIGN KEY (from_id) REFERENCES users (id),
    FOREIGN KEY (to_id) REFERENCES users (id)
    )
    """
    try:
        cursor_second.execute(query)
    except errors.DuplicateTable:
        print("The Table exists")

def delete_table(name, cursor_second):
    query = f"""
        DROP TABLE '{name}'; 
        """
    try:
        cursor_second.execute(query)
    except psycopg2.ProgrammingError as error:
        print("Tabela istnieje: ", error)

def delete_db(name, cursor):
    query = f"""
        DROP DATABASE {name}; 
        """
    try:
        cursor.execute(query)
    except psycopg2.ProgrammingError as error:
        print("Tabela istnieje: ", error)
