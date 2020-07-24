from cryptography.fernet import Fernet
#do not edit this key
KEY = "ehKMdrFs2lSkLLiYxaRbABogh6XW4HUfeV0ogsrFaYM="


class EncryptorAndDecryptor:

    def encode(self, plainText):
        message = plainText.encode()
        f = Fernet(self.getBytes(string=KEY))
        return f.encrypt(message).decode()

    def decode(self, chiperText):
        f = Fernet(self.getBytes(string=KEY))
        return f.decrypt(self.getBytes(string=chiperText)).decode()

    def getBytes(self, string):
        return bytes(string, "ascii")
