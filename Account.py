from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512 as SHA512
import random

random.seed(24081991)

def genID():  # уникальный айди аккаунта будет генерироваться с реализацией класса блокчейн
    return random.randint(10000000, 99999999)

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

class Signature:
    def signData(self, plaintext, key, hash_algorithm=SHA512):
        plaintext = str(plaintext).encode(encoding='utf-8')
        signer = PKCS1_v1_5.new(RSA.importKey(key))
        hash_value = hash_algorithm.new(plaintext)
        return signer.sign(hash_value)

    def verifySignature(self, sign, plaintext, key, hash_algorithm=SHA512):
        plaintext = str(plaintext).encode(encoding='utf-8')
        hash_value = hash_algorithm.new(plaintext)
        verifier = PKCS1_v1_5.new(RSA.importKey(key))
        return verifier.verify(hash_value, sign)

class Account:
    def __init__(self):
        self.genAccount()

    def genAccount(self):
        Keys = KeyPair()
        self.wallets = []
        self.property = dict()
        self.wallets.append(Keys.genKeyPair())
        self.accountID = genID()
        return self.wallets, self.accountID

    def addKeyPairToWallet(self):
        self.wallets.append(A.genKeyPair())

    def signtext(self, text, index):
        Sign = Signature()
        key = self.wallets[index][1]
        return Sign.signData(text, key)

    def addProp(self, cadastral_number):
        self.property[cadastral_number] = self.accountID

    def delProp(self, cadastral_number):
        if self.property.get(cadastral_number) != None:
            del self.property[cadastral_number]

    def getBalance(self):
        return list(self.property.keys())

    def printBalance(self):
        print(f"Account №{self.accountID} property:")
        property = list(self.property.keys())
        for i in range(len(property)):
            print(f'{i + 1}) "{property[i]}"')

B = Account()
B.addProp(19)
B.addProp(91)
B.addProp(11)
B.printBalance()
B.delProp(191)
B.delProp(19)
B.printBalance()

print("----------------")

A = Signature()
User = Account()
User.genAccount()
message = "message for test"
sign = User.signtext(message, 0)
print(A.verifySignature(sign, message, User.wallets[0][0]))