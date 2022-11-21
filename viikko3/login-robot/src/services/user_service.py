from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if username in self._user_repository.find_all():
            raise UserInputError("Username taken")

        if len(username) < 4:
            raise UserInputError("Too short a username")

        if len(password) < 8:
            raise UserInputError("Too short a password")

        if re.search("[0-9]", password) and re.search("[a-zA-Z]", password):
            pass
        else:
            raise UserInputError("Password too simple")


        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
