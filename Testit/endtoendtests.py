import unittest
from create_keys import create_new_RSA_keys
from encryptions import encrypt_message,decrypt_message
from message_objects import Message

class TestCreateKeysThenEncryptThenDecrypt(unittest.TestCase):
    """Create keys, encrypt a message with one key and decrypt it with the other key"""
    def test_create_keys_encrypt_with_secret_key_then_decrypt(self):
        RSA_keys = create_new_RSA_keys(1024)
        encrypted_message = encrypt_message(Message('E2Etesti: salainen avain salaa',False),RSA_keys[0])
        decrypted_message = decrypt_message(encrypted_message,RSA_keys[1])
        self.assertEqual(decrypted_message.message_content,'E2Etesti: salainen avain salaa')

    def test_create_keys_encrypt_with_public_key_then_decrypt(self):
        RSA_keys = create_new_RSA_keys(1024)
        encrypted_message = encrypt_message(Message('E2Etesti: julkinen avain salaa',False),RSA_keys[1])
        decrypted_message = decrypt_message(encrypted_message,RSA_keys[0])
        self.assertEqual(decrypted_message.message_content,'E2Etesti: julkinen avain salaa')

if __name__ == '__main__':
    unittest.main()
