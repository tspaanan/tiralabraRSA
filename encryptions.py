import key_objects
from message_objects import Message

def encrypt_message(message, key):
    message_content_str = message.message_content
    message_content_byt = message_content_str.encode()
    print(str(message_content_byt))
    #message_content_int = int(''.join(map(str,list(message_content_byt))))
    #tähän väliin message padding
    message_content_int = int.from_bytes(message_content_byt,'big')
    print(message_content_int)
    encrypted_message_content_int = pow(message_content_int,key.exponent,key.modulus_n)
    print(encrypted_message_content_int)
    #encrypted_message_content_byt = encrypted_message_content_int.to_bytes(encrypted_message_content_int.bit_length(),'big')
    #print(encrypted_message_content_byt)
    #encrypted_message = Message(encrypted_message_content_byt,True)
    encrypted_message = Message(encrypted_message_content_int,True)
    return encrypted_message

def decrypt_message(message, key):
    #message_content_str = message.message_content
    #message_content_byt = message_content_str.encode()
    #message_content_byt = message.message_content
    #message_content_int = int.from_bytes(message_content_byt,'big')
    message_content_int = message.message_content
    decrypted_message_content_int = pow(message_content_int,key.exponent,key.modulus_n)
    decrypted_message_content_byt = decrypted_message_content_int.to_bytes((decrypted_message_content_int.bit_length()+7)//8,'big')
    decrypted_message = Message(decrypted_message_content_byt.decode(),False)
    return decrypted_message
