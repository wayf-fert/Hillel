import re


class NameDescriptor:
    def __init__(self, name: str):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get("name", None)

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{self.name.capitalize()} must be a non-empty string")
        instance.__dict__["name"] = value

    def __delete__(self, instance):
        raise AttributeError("Name cannot be deleted")


class EmailDescriptor:
    def __init__(self, email: str):
        self.name = email

    def __get__(self, instance, owner):
        return instance.__dict__.get("email", None)

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Email must be not empty string")
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format")
        instance.__dict__["email"] = value

    def __delete__(self, instance):
        raise AttributeError("Email cannot be deleted")


class AddressDescriptor:
    def __init__(self, address: str):
        self.address = address

    def __get__(self, instance, owner):
        return instance.__dict__.get("address", None)

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Address must be not empty")
        instance.__dict__["address"] = value

    def __delete__(self, instance):
        raise AttributeError("Address cannot be deleted")


class Person:
    name = NameDescriptor("name")
    email = EmailDescriptor("email")
    address = AddressDescriptor("address")

    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name our hero is {self.name}. He has email: \"{self.email}\" and live in {self.address}"


# Приклад використання:
person = Person("John Dou", "lysiy.john@example.com", "Kyiv, Example str, 1")
print(person)
