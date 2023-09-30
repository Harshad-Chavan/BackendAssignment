import jwt
import datetime
from django.conf.global_settings import SECRET_KEY


class Auth:

    # create JWT
    @staticmethod
    def createJWT(username):
        """
        this method creates the jwt tokoen that will be sent ot the requesting user after validation of username & password.
        this jwt token will be used by the user for subsequent requests.
        jwt token comprises header, payload

        :param username:
        :param secret:
        :param authz:
        :return:
        """
        return jwt.encode(
            # Payload
            {
                "username": username,
                "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1),
                "iat": datetime.datetime.utcnow(),

            },
            # JWT secret Key
            SECRET_KEY,
            algorithm="HS256",
        )

    # Parse JWT
    def validate(self, request):
        encoded_jwt = request.headers["Authorization"]

        if not encoded_jwt:
            return "missing credentials", 401

        encoded_jwt = encoded_jwt.split(" ")[1]

        try:
            decoded = jwt.decode(encoded_jwt, SECRET_KEY, algorithms="HS256")
        except:
            return "Not authorized"

        return decoded
