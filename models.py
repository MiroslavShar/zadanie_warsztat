class User:
    def __init__(self, _id=1, username, _hashed_password):
        self._id = _id
        self._hashed_password = _hashed_password

    def new_password(self, ):