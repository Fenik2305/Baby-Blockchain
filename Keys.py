from Crypto.PublicKey import RSA

class KeyPair:
    def genKeyPair(self):
        privatekey = RSA.generate(2048)
        publickey = privatekey.publickey()
        self.privatekey = privatekey.exportKey(format='PEM')
        self.publickey = publickey.exportKey(format='PEM')
        return [self.publickey, self.privatekey]

    def __init__(self):
        keys = self.genKeyPair()
        self.publickey, self.privatekey = keys[0], keys[1]

    def printKeyPair(self):
        print(f'PublicKey = {self.publickey}\nPrivateKey = {self.privatekey}')

    def __str__(self):
        return f'{self.privatekey} {self.publickey}'

from Crypto.PublicKey import RSA

class KeyPair:
    def genKeyPair(self):
        privatekey = RSA.generate(2048)
        publickey = privatekey.publickey()
        self.privatekey = privatekey.exportKey(format='PEM')
        self.publickey = publickey.exportKey(format='PEM')
        return [self.publickey, self.privatekey]

    def __init__(self):
        keys = self.genKeyPair()
        self.publickey, self.privatekey = keys[0], keys[1]

    def printKeyPair(self):
        print(f'PublicKey = {self.publickey}\nPrivateKey = {self.privatekey}')

    def __str__(self):
        return f'{self.privatekey} {self.publickey}'

KEYS = KeyPair()
KEYS.genKeyPair()
KEYS.printKeyPair()
