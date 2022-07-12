import jwt
from flask import request, abort

from constants import JWT_ALG, JWT_SECRET

def auth_required(func):
    def wrapper(*args, **kwargs):
        if not 'Authorization' in request.headers:
            abort(401)

        token = request.headers['Authorization']
        try:
            jwt.decode(token, JWT_SECRET, algorithm=[JWT_ALG])
        except Exception as e:
            print(f'JWT decode error: {e}')
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if not 'Authorization' in request.headers:
            abort(401)

        token = request.headers['Authorization']
        try:
            data = jwt.decode(token, JWT_SECRET, algorithm=[JWT_ALG])
        except Exception as e:
            print(f'JWT decode error: {e}')
            abort(401)
        else:
            if data['role'] == 'admin':
                return func(*args, **kwargs)
        abort(403)

    return wrapper
