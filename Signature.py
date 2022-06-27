from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512 as SHA512

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

A = Signature()
message = 1231244
keys = RSA.generate(2048)
privatekey = keys.exportKey(format='PEM')
publickey = keys.publickey().exportKey(format='PEM')
sign = A.signData(message, privatekey)
print(A.verifySignature(sign, message, publickey))