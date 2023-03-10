import argparse
import io
import unittest
from create_keys import create_new_RSA_keys
from encryptions import encrypt_message,decrypt_message
import key_objects
from message_objects import Message
import Testit.verifytests

cli_parser = argparse.ArgumentParser(description='CLI for tiralabraRSA: create RSA keys, encrypt and decrypt messages')

cli_parser.add_argument('--create_keys', action='store_true', help='create new RSA keys with variable length')
cli_parser.add_argument('--key_length', action='store', type=int, default=1024, help='length of RSA keys in bits (default: 1024)')
cli_parser.add_argument('--encrypt', action='store_true', help='encrypt a message')
cli_parser.add_argument('--decrypt', action='store_true', help='decrypt a message')
cli_parser.add_argument('--message', action='store', help='message to be encrypted')
cli_parser.add_argument('--key', action='store', help='key file used for encryption or decryption')
cli_parser.add_argument('--input', action='store', help='input file used to read the message from')
cli_parser.add_argument('--output', action='store', help='output file used to write the results into')
cli_parser.add_argument('--no_padding', action='store_true', help='whether to use random padding in messages for security or not')
cli_parser.add_argument('--verify', action='store_true', help='verify the validity of new RSA keys')

cli_args = cli_parser.parse_args()

if cli_args.create_keys:
    keys = create_new_RSA_keys(cli_args.key_length)
    if cli_args.verify:
        verify_tests = unittest.TestLoader().loadTestsFromModule(Testit.verifytests)
        verify_results = unittest.TextTestRunner(stream=io.StringIO(),buffer=True).run(verify_tests)
        if not verify_results.wasSuccessful():
            print('Created keys have not passed verification. Please create a new key pair.')

if cli_args.encrypt:
    with open(cli_args.key,'r') as key_file:
        key_object = key_objects.GenericKey(int(key_file.readline().strip()),int(key_file.readline().strip()))
    random_padding = not cli_args.no_padding
    if cli_args.message:
        encrypted_message = encrypt_message(Message(cli_args.message,False),key_object,random_padding=random_padding)
    else:
        with open(cli_args.input,'r') as input_file:
            encrypted_message = encrypt_message(Message(input_file.read(),False),key_object,random_padding=random_padding)
    with open(cli_args.output,'w') as encrypted_message_file:
        encrypted_message_file.write(f'{str(encrypted_message.message_content)}\n')

if cli_args.decrypt:
    with open(cli_args.key,'r') as key_file:
        key_object = key_objects.GenericKey(int(key_file.readline().strip()),int(key_file.readline().strip()))
    with open(cli_args.input,'r') as enc_message_file:
        message_int = int(enc_message_file.readline().strip())
    dec_message = decrypt_message(Message(message_int,True),key_object)
    if cli_args.output == 'screen':
        print(dec_message)
    else:
        with open(cli_args.output,'w') as dec_message_file:
            dec_message_file.write(f'{dec_message.message_content}\n')
