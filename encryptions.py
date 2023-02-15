import key_objects
from message_objects import Message

def encrypt_message(message, key):
    message_content_str = message.message_content
    message_content_byt = message_content_str.encode()
    
    #tähän väliin message padding
    
    message_content_int = int.from_bytes(message_content_byt,'big')
    encrypted_message_content_int = pow(message_content_int,key.exponent,key.modulus_n)
    encrypted_message = Message(encrypted_message_content_int,True)
    print('Encrypted message')
    return encrypted_message

def decrypt_message(message, key):
    message_content_int = message.message_content
    decrypted_message_content_int = pow(message_content_int,key.exponent,key.modulus_n)
    decrypted_message_content_byt = decrypted_message_content_int.to_bytes((decrypted_message_content_int.bit_length()+7)//8,'big')
    decrypted_message = Message(decrypted_message_content_byt.decode(),False)
    print('Decrypted message')
    return decrypted_message

#testing random padding
def encrypt_with_random_padding(message, key):
    #random padding, cannot have b'00' anywhere in it!
    #following https://www.rfc-editor.org/rfc/rfc8017
    PS = b'01234567'
    #encoded message
    EM = b'00' + b'02' + PS + b'00' + message.message_content.encode()
    #message as integer
    m = int.from_bytes(EM,'big')
    print(f'plain-text int: {m}')
    #encrypted message as integer
    encrypted_message_content_int = pow(m,key.exponent,key.modulus_n)
    print(f'encrypted int: {encrypted_message_content_int}')
    return Message(encrypted_message_content_int,True)

def decrypt_with_random_padding(message, key):
    #begin decryption from encrypted_message_content_int
    decrypted_message_content_int = pow(message.message_content,key.exponent,key.modulus_n)
    print(f'decrypted message as integer: {decrypted_message_content_int}')
    decrypted_message_content_byt = decrypted_message_content_int.to_bytes((decrypted_message_content_int.bit_length()+7)//8,'big')
    #stripping 0x00 and 0x02
    stripped_prefix = decrypted_message_content_byt.lstrip(b'0020')
    #stripping random padding
    orig_byte_str = stripped_prefix.split(b'00')[1]
    decrypted_message = Message(orig_byte_str.decode(),False)
    return decrypted_message