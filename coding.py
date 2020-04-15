
import hashlib, binascii, os
class coding:
    def hash_password(self, password):
        return hashlib.sha224(password.encode()).hexdigest()
