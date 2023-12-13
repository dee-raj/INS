import hashlib
class SHA1:
   def __init__(self, msg):
      self.msg = msg

   def encode_hex(self):
      result = hashlib.sha1(self.msg.encode())
      print(f"The hexadecimal equivalent of SHA is: {result.hexdigest()}")

if __name__ == "__main__":
   msg = input("Enter the value to encode: ")
   sha = SHA1(msg)
   sha.encode_hex()