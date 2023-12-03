from flask import request, jsonify
import jwt
from functools import wraps
import os

def verify_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('userToken')

        if not token:
            return jsonify({'message': 'Token not provided'}), 401

        try:
            decoded = jwt.decode(token.replace('Bearer ', ''), os.environ.get('SECRET_KEY'), algorithms=['HS256'])
            # Replace 'your_secret_key' with the actual secret key used for signing tokens

            # Attach the decoded user to the request object
            request.user = decoded
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token Expired: Try logging in again'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid Token: Try logging in again'}), 401

        return func(*args, **kwargs)

    return wrapper
