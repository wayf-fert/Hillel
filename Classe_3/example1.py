class NameDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("name", None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Students value must be of type str")
        if not value.strip():
            raise ValueError("Students value must not be empty")
        instance.__dict__["name"] = value.strip()

    def __delete__(self, instance):
        raise AttributeError("Student cannot be deleted")


class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("age", None)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Student value must be of type int")
        if value < 18:
            raise ValueError("Student value must be greater than 18")
        instance.__dict__["age"] = value

    def __delete__(self, instance):
        raise AttributeError("Student cannot be deleted")


class Student:
    name = NameDescriptor()
    age = AgeDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


s1 = Student("John Dou", 27)
print(s1)
