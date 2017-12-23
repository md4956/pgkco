from werkzeug.security import generate_password_hash, check_password_hash


class security(object):
    @staticmethod
    def set_password(password):
        return generate_password_hash(password, salt_length=32)

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)
