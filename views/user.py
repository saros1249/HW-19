from flask import request, make_response
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service
from service.decorators import admin_required

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    schema = UserSchema(many=True)

    @admin_required
    def get(self):
        return self.schema.dump(user_service.get_all()), 200

    def post(self):
        user = user_service.create(request.json)
        res = make_response('Новый пользователь добавлен', 201)
        res.headers['location'] = f'{user_ns.path}/{user.id}'
        return res


@user_ns.route('/<int:uid>')
class UserView(Resource):
    schema = UserSchema

    @admin_required
    def put(self, uid: int):
        user = self.schema.dump(user_service.update(uid, request.json))
        return f'Запись с ID{uid} изменена на {user}.', 200

    @admin_required
    def delete(self, uid: int):
        user_service.delete(uid)
        return 204
