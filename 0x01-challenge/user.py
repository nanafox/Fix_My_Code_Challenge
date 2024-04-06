#!/usr/bin/python3
"""
User class
"""


class User:
    """Defines the user class."""

    def __init__(self):
        """Initializes the User instance."""
        self.email = ""

    @property
    def email(self):
        """Returns the email address."""
        return self.__email

    @email.setter
    def email(self, value):
        """Sets the email address."""
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
