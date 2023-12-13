import hashlib
class msgDigest:
   def __init__(self, original_msg:bytes):
      self.msg = original_msg

   def sender_useMD(self):
      self.sender = hashlib.md5(self.msg)
      self.md_is_sent = self.sender.digest()
      print(f"The byte equivalance of {self.sender} \nSender's hash is: {self.md_is_sent}\n")

   def attacker(self, modify_msg:bytes):
      print(f"msg before attack: {self.msg}.")
      self.msg = modify_msg
      print(f"msg after attack: {self.msg}.\n")

   def receiver_useMD(self):
      self.receiver = hashlib.md5(self.msg)
      self.md_is_got = self.receiver.digest()
      print(f"The byte equivalance of {self.receiver} \nReceiver's hash is: {self.md_is_got}\n")

   def result(self):
      print("same message") if self.md_is_sent == self.md_is_got else print("modified message")

if __name__ == "__main__":
   md = msgDigest(b'jai shri krishna')
   md.sender_useMD()
   md.attacker(b'jai shree krishna')
   md.receiver_useMD()
   md.result()

"""OUTPUT:-
The byte equivalance of <md5 _hashlib.HASH object @ 0x0000025BA823ABF0> 
Sender's hash is: b'\xb76\xfcb\xbb^5\xee\xdf\x89\t\x82\x9d+\xb6\x88'    

msg before attack: b'jai shri krishna'.
msg after attack: b'Jai shree Krishna'.

The byte equivalance of <md5 _hashlib.HASH object @ 0x0000025BA823BCF0> 
Receiver's hash is: b'g9\x14,\xa3G\x8a{\x19\x0e|\xc5c\x83u\xd6'

modified message
"""
