from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Получение жанра по ID.
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Получение списка всех жанров.
        """
        return self.dao.get_all()

    def create(self, genre_d):
        """
        Создание новой записи.
        """
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """
        Редактирование записи в БД.
        """
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        """
        Удаление записи по ID.
        """
        self.dao.delete(rid)
