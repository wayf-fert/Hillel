import re


class User:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("First name must be a non-empty string")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Last name must be a non-empty string")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Email must be a non-empty string")
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format")
        self._email = value

    def __str__(self):
        return (f"User: {self.first_name} {self.last_name},\n"
                f"Email: {self.email}")


user = User("John", "Dou", "lysiy.type@example.com")
print(user)
