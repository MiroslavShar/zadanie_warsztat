from connect import connect
import hashlib

class User:
    def __init__(self, username="", password="", salt=""):
        self._id = -1
        self._hashed_password = hash_password(password, salt)
        username = username

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password
    def set_password(self, password, salt="", cursor):
        self._hashed_password =  hash_password(password, salt)

    def save_to_db(self, ):
        pass

    def load_user_by_username(self, username, cursor):
        query = f"""
        SELECT * FROM users,
        WHERE username = {username}
        """
        cursor.execute(query)


    def load_user_by_id(self, id, cursor):
        query = f"""
        SELECT * FROM users,
        WHERE id = {id}
        """
        cursor.execute(query)

    def load_all_users(self, cursor):
        pass



