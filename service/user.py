import base64
import hashlib
import hmac

from constants import *
from dao.user import UserDAO


class UserService():
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        """
        Получение пользователя по ID.
        """
        return self.dao.get_one(uid)

    def get_all(self):
        """
        Получение списка всех пользователей.
        """
        return self.dao.get_all()

    def get_by_username(self, username):
        """
        Получения пользователя по имени.
        """
        return self.dao.get_by_username(username)

    def create(self, user_d):
        """
        Создание нового пользователя.
        """
        return self.dao.create(user_d)

    def update(self, user_d):
        """
        Редактирование записи пользователя в БД.
        """
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        """
        Удаление пользователя по ID.
        """
        self.dao.delete(uid)

    def get_password_hash(self, password):
        """
        Создание хэша пароля.
        """
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password, password_hash):
        """
        Проверка введённого пароля.
        """
        return hmac.compare_digest(base64.b64decode(self.get_password_hash(password_hash)),
                                   base64.b64decode(self.get_password_hash(password)))
