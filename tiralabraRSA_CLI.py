import argparse
from create_keys import create_new_RSA_keys
from encryptions import encrypt_message,decrypt_message
import key_objects
from message_objects import Message

# https://docs.python.org/3/library/argparse.html

cli_parser = argparse.ArgumentParser(description='CLI for tiralabraRSA: create RSA keys, encrypt and decrypt messages')

#lisätään yhteyksiä näiden välille, esim. encrypt ei voi käyttää ilman avainta
cli_parser.add_argument('--create_keys', action='store_true', help='create new RSA keys with variable length')
cli_parser.add_argument('--key_length', action='store', type=int, default=1024, help='length of RSA keys in bits (default: 1024)')
cli_parser.add_argument('--encrypt', action='store_true', help='encrypt a message')
cli_parser.add_argument('--decrypt', action='store_true', help='decrypt a message')
cli_parser.add_argument('--message', action='store', type=str, help='message to be encrypted or decrypted')
cli_parser.add_argument('--key', action='store', type=str, help='keyfile used for encryption or decryption')

cli_args = cli_parser.parse_args()

if cli_args.create_keys:
    create_new_RSA_keys(cli_args.key_length)

if cli_args.encrypt:
    #print(cli_args.key)
    with open(cli_args.key,'r') as key_file:
        key_object = key_objects.GenericKey(int(key_file.readline().strip()),int(key_file.readline().strip()))       #print(key_file.readline().strip(),key_file.readline().strip())
        print(key_object.modulus_n)
        print(key_object.exponent)
    enc_message = encrypt_message(Message("testi",False),key_object)
    print(enc_message)
    with open('encrypted_message','w') as enc_message_file:
        enc_message_file.write(enc_message.message_content.hex())

if cli_args.decrypt:
    with open(cli_args.key,'r') as key_file:
        key_object = key_objects.GenericKey(int(key_file.readline().strip()),int(key_file.readline().strip()))       #print(key_file.readline().strip(),key_file.readline().strip())
    with open(cli_args.message,'r') as enc_message_file:
        message_bytes = bytes.fromhex(enc_message_file.readline())
    dec_message = decrypt_message(Message(message_bytes,True),key_object)
    print(dec_message)

