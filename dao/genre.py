from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        Получение жанра по ID.
        """
        return self.session.query(Genre).get(bid)

    def get_all(self):
        """
        Получение списка всех жанров.
        """
        return self.session.query(Genre).all()

    def create(self, genre_d):
        """
        Создание новой записи.
        """
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Удаление записи по ID.
        """
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        """
        Редактирование записи в БД.
        """
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
