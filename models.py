from connect import connect, connect_second
import hashlib
from clcrypto import generate_salt, hash_password, check_password

class User:
    def __init__(self, username="", password="", salt=""):
        self._id = -1
        self._hashed_password = hash_password(password, salt)
        self.username = username


    @property
    def id(self):
        return self._id


    @property
    def hashed_password(self):
        return self._hashed_password


    def set_password(self, password, salt=""):
        self._hashed_password = hash_password(password, salt)


    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)


    def save_to_db(self, cursor_second):
        if self._id == -1:
            query = """
            INSERT INTO users(username, hashed_password)
            VALUES (%s, %s) 
            RETURNING id;
            """
            values = (self.username, self.hashed_password)
            cursor_second.execute(query, values)
            self._id = cursor_second.fetchone()[0]
            return True
        return False


    @staticmethod
    def load_user_by_username(cursor_second, username_new):
        query = f"""
        SELECT *
        FROM users
        WHERE username = '{username_new}';
        """
        cursor_second.execute(query)
        data = cursor_second.fetchone()
        if data:
            id_, username, hash_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hash_password
            return loaded_user
        else:
            return None


    @staticmethod
    def load_user_by_id(cursor_second, id_):
        query = f"""
        SELECT id, username, hashed_password
        FROM users
        WHERE id = {id_};
        """
        cursor_second.execute(query)
        data = cursor_second.fetchone()
        if data:
            id_, username, hash_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hash_password
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor_second):
        query = """
        SELECT id, username, hashed_password
        FROM users; 
        """
        users = []
        cursor_second.execute(query)
        for row in cursor_second.fetchall():
            id_, username, hashed_password = row
            loaded_user = User()
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            users.append(loaded_user)
        return users


    def __str__(self):
        return str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

