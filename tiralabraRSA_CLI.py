import argparse
from create_keys import create_new_RSA_keys
from encryptions import encrypt_message,decrypt_message
import key_objects
from message_objects import Message
#debug
from encryptions import encrypt_with_random_padding,decrypt_with_random_padding

cli_parser = argparse.ArgumentParser(description='CLI for tiralabraRSA: create RSA keys, encrypt and decrypt messages')

cli_parser.add_argument('--create_keys', action='store_true', help='create new RSA keys with variable length')
cli_parser.add_argument('--key_length', action='store', type=int, default=1024, help='length of RSA keys in bits (default: 1024)')
cli_parser.add_argument('--encrypt', action='store_true', help='encrypt a message')
cli_parser.add_argument('--decrypt', action='store_true', help='decrypt a message')
cli_parser.add_argument('--message', action='store', help='message to be encrypted')
cli_parser.add_argument('--key', action='store', help='key file used for encryption or decryption')
cli_parser.add_argument('--input', action='store', help='input file used to read the message from')
cli_parser.add_argument('--output', action='store', help='output file used to write the results into')
cli_parser.add_argument('--padding', action='store_true', help='whether to use random padding in messages for security or not')

cli_args = cli_parser.parse_args()

if cli_args.create_keys:
    create_new_RSA_keys(cli_args.key_length)

if cli_args.encrypt:
    with open(cli_args.key,'r') as key_file:
        key_object = key_objects.GenericKey(int(key_file.readline().strip()),int(key_file.readline().strip()))
    if cli_args.message:
        encrypted_message = encrypt_message(Message(cli_args.message,False),key_object)
    else:
        with open(cli_args.input,'r') as input_file:
            encrypted_message = encrypt_message(Message(input_file.read(),False),key_object)
    with open(cli_args.output,'w') as encrypted_message_file:
        encrypted_message_file.write(f'{str(encrypted_message.message_content)}\n')

if cli_args.decrypt:
    with open(cli_args.key,'r') as key_file:
        key_object = key_objects.GenericKey(int(key_file.readline().strip()),int(key_file.readline().strip()))
    with open(cli_args.input,'r') as enc_message_file:
        message_int = int(enc_message_file.readline().strip())
    dec_message = decrypt_message(Message(message_int,True),key_object)
    with open(cli_args.output,'w') as dec_message_file:
        dec_message_file.write(f'{dec_message.message_content}\n')
    print(dec_message)

#testing random padding
if cli_args.padding:
    with open(cli_args.key,'r') as key_file:
        key_object = key_objects.GenericKey(int(key_file.readline().strip()),int(key_file.readline().strip()))
    padded_message = encrypt_with_random_padding(Message("padding_testi",False),key_object)
    print(padded_message)
    with open('public_key','r') as key_file:
        key_object = key_objects.GenericKey(int(key_file.readline().strip()),int(key_file.readline().strip()))
    print(decrypt_with_random_padding(padded_message,key_object))
