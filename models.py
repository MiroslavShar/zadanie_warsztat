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
        else:
            query = """
            UPDATE users SET username=%s, hashed_password=%s
            WHERE id=%s
            """
            values = (self.username, self.hashed_password, self._id)
            cursor_second.execute(query, values)
            return True
    @staticmethod
    def edit_password(cursor_second, id_user, new_username, new_password):
        query = f"""
        UPDATE users SET username=%s, hashed_password=%s
        WHERE id=%s
        """
        values = (new_username, new_password, id_user)
        cursor_second.execute(query, values)
        return True

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

    def delete(self, cursor_second):
        query = f"""
        DELETE FROM users 
        WHERE username = %s; 
        """
        cursor_second.execute(query, (self.username,))
        self._id = -1
        return True

    class Messages:
        def __init__(self, from_id, to_id, text):
            self._id = -1
            self.creation_data = None
            self.to_id = to_id
            self.from_id = from_id
            self.text = text

        @property
        def id(self):
            return self._id

        def save_to_db(self, cursor_second):
            if self._id == -1:
                query = """
                INSERT INTO messages (from_id, to_id, creation_date, text)
                VALUES (%s, %s, %s, %s,)
                RETURNING ID;
                """
                values = (self.from_id, self.to_id, self.creation_data, self.text)
                cursor_second.execute(query, values)
                self._id = cursor_second.fetchone()[0]
                return True
            else:
                query = """
                UPDATE messages 
                SET from
                """


    def __str__(self):
        return str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def __repr__(self):
        return str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
