from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

privKey = keyPair
print(f"Private key: (n={hex(privKey.n)}, d={hex(privKey.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))


# encryption
msg = "good morning"
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode('utf-8'))
print(f"Encripted: {binascii.hexlify(encrypted)}")

#decryption
decryptor = PKCS1_OAEP.new(privKey)
decrypted = decryptor.decrypt(encrypted)
print("Plain text: ", decrypted.decode('utf-8'))
