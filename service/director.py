from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Получение режиссёра по ID
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Получение списка всех режиссёров.
        """
        return self.dao.get_all()

    def create(self, director_d):
        """
        Создание новой записи в БД.
        """
        return self.dao.create(director_d)

    def update(self, director_d):
        """
        Удаление записи по ID.
        """
        self.dao.update(director_d)
        return self.dao

    def delete(self, rid):
        """
        Редактирование записи.
        """
        self.dao.delete(rid)
