import rsa
from Cryptodome.Cipher import AES
import requests
import base64
import winreg
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\EasyRSA", 0, winreg.KEY_READ)
aeskey, regtype = winreg.QueryValueEx(key, "key")
aeskey = bytes(aeskey, 'utf-8')
print("AES Key: " + str(aeskey))
# Generate new keys
(pubkey, privkey) = rsa.newkeys(512)
# Encrypt keys
pubkey = base64.b64encode(pubkey.save_pkcs1())
privkey = base64.b64encode(privkey.save_pkcs1())
print("Public Key: " + str(pubkey))
print("Private Key: " + str(privkey))
aes1 = AES.new(aeskey, AES.MODE_EAX, nonce=b'1234567890123456')
ciphertext1 = aes1.encrypt(pubkey)
aes2 = AES.new(aeskey, AES.MODE_EAX, nonce=b'1234567890123456')
ciphertext2 = aes2.encrypt(privkey)
print("Encrypted Public Key: " + str(ciphertext1))
print("Encrypted Private Key: " + str(ciphertext2))

# Now reverse

print("In reverse")

aes1 = AES.new(aeskey, AES.MODE_EAX, nonce=b'1234567890123456')
pubkey = aes1.decrypt(ciphertext1)
aes2 = AES.new(aeskey, AES.MODE_EAX, nonce=b'1234567890123456')
privkey = aes2.decrypt(ciphertext2)
print("Public Key: " + str(pubkey))
print("Private Key: " + str(privkey))
# Decode base64
pubkey = base64.b64decode(pubkey)
privkey = base64.b64decode(privkey)
print("Public Key: " + str(pubkey))
print("Private Key: " + str(privkey))
