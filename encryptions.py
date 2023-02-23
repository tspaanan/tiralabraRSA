import secrets
import string
import key_objects
from message_objects import Message

def encrypt_message(message, key, suppress_output=False, random_padding=True):
    message_content_str = message.message_content
    message_content_byt = message_content_str.encode()
    
    if random_padding:
        padding_length = max(8, (key.modulus_n.bit_length() // 8) - len(message_content_byt) - 3)
        PS = ''.join(secrets.choice(string.ascii_letters) for _ in range(padding_length)).encode()
        EM = int.to_bytes(0,1,'big') + int.to_bytes(2,1,'big') + PS + int.to_bytes(0,1,'big') + message.message_content.encode()
        message_content_int = int.from_bytes(EM,'big')
    else:
        message_content_int = int.from_bytes(message_content_byt,'big')
    
    encrypted_message_content_int = pow(message_content_int,key.exponent,key.modulus_n)
    encrypted_message = Message(encrypted_message_content_int,True)
    if not suppress_output:
        print('Encrypted message')
    return encrypted_message

def decrypt_message(message, key, suppress_output=False):
    message_content_int = message.message_content
    decrypted_message_content_int = pow(message_content_int,key.exponent,key.modulus_n)
    decrypted_message_content_byt = decrypted_message_content_int.to_bytes((decrypted_message_content_int.bit_length()+7)//8,'big')

    if decrypted_message_content_byt.startswith(b'\x02'):
        stripped_prefix = decrypted_message_content_byt.lstrip(b'\x00\x02')
        orig_byte_str = stripped_prefix.split(b'\x00')[1]
        decrypted_message = Message(orig_byte_str.decode(),False)
    else:
        decrypted_message = Message(decrypted_message_content_byt.decode(),False)
    
    if not suppress_output:
        print('Decrypted message')
    return decrypted_message
