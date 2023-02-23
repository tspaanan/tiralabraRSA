import unittest
import secrets
import string
from encryptions import encrypt_message,decrypt_message
import key_objects
from message_objects import Message

class TestVerifyCreatedKeys(unittest.TestCase):
    """Verify that newly created key pair functions properly"""
    def test_verify_created_keys(self):
        with(open('secret_key','r')) as secret_key_file:
            secret_key = key_objects.SecretKey(int(secret_key_file.readline().strip()),int(secret_key_file.readline().strip()))
        with(open('public_key','r')) as public_key_file:    
            public_key = key_objects.SecretKey(int(public_key_file.readline().strip()),int(public_key_file.readline().strip()))
        RSA_keys = (secret_key,public_key)
        msg_length_byt = min(secret_key.modulus_n.bit_length(),secret_key.exponent.bit_length(),public_key.exponent.bit_length()) // 8
        for _ in range(10):
            long_rnd_message = ''.join(secrets.choice(string.ascii_letters) for _ in range(msg_length_byt))
            encrypted_message = encrypt_message(Message(long_rnd_message,False),RSA_keys[0],True,False)
            decrypted_message = decrypt_message(encrypted_message,RSA_keys[1],True)
            self.assertEqual(decrypted_message.message_content,long_rnd_message)
            encrypted_message = encrypt_message(Message(long_rnd_message,False),RSA_keys[1],True,False)
            decrypted_message = decrypt_message(encrypted_message,RSA_keys[0],True)
            self.assertEqual(decrypted_message.message_content,long_rnd_message)

if __name__ == '__main__':
    unittest.main()
