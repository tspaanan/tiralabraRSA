from enum import Enum

class KeyClass(Enum):
    GENERIC = 'generic'
    PUBLIC = 'public'
    SECRET = 'secret'

class GenericKey:
    def __init__(self, modulus_n, exponent):
        self.keyclass = KeyClass.GENERIC
        self.modulus_n = modulus_n
        self.exponent = exponent

    def __str__(self):
        return f'KeyClass: {self.keyclass.value}'

class PublicKey(GenericKey):
    def __init__(self, modulus_n, exponent):
        super().__init__(modulus_n, exponent)
        self.keyclass = KeyClass.PUBLIC

class SecretKey(GenericKey):
    def __init__(self, modulus_n, exponent):
        super().__init__(modulus_n, exponent)
        self.keyclass = KeyClass.SECRET