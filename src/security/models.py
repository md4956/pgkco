from werkzeug.security import generate_password_hash, check_password_hash


class security(object):
    @staticmethod
    def set_password(password):
        return generate_password_hash(password, salt_length=32)

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)
#
# class security(object):
#
#     def __init__(self, username, password):
#         self.username = username
#         self.set_password(password)
#
#     def set_password(self, password):
#         self.pw_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.pw_hash, password)
#
