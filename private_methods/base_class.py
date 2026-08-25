class BaseClases:
    def __init__(self):
        self._protected_variable = "This is a protected variable"

    def __private_method(self):
        return "This is a private method"

    def public_method(self):
        return self.__private_method()

    def _protected_method(self):
        return "This is a protected method"


base = BaseClases()

print(base._protected_variable)
print(base._protected_method())
