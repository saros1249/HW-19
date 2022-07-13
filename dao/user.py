from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """
        Получение пользователя по ID.
        """
        return self.session.query(User).get(uid)

    def get_all(self):
        """
        Получение списка всех пользователей.
        """
        return self.session.query(User).all()

    def get_by_username(self, username):
        """
        Получения пользователя по имени.
        """
        return self.session.query(User).filter(User.username == username).first()

    def create(self, user_d):
        """
        Создание нового пользователя.
        """
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Удаление пользователя по ID.
        """
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        """
        Редактирование записи пользователя в БД.
        """
        user = self.get_one(user_d.get("id"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get("role")
        self.session.add(user)
        self.session.commit()
