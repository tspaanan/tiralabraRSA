import argparse
from create_keys import create_new_RSA_keys

# https://docs.python.org/3/library/argparse.html

cli_parser = argparse.ArgumentParser(description='CLI for tiralabraRSA: create RSA keys, encrypt and decrypt messages')

cli_parser.add_argument('--create_keys', action='store_true', help='create new RSA keys with variable length')
cli_parser.add_argument('--key_length', action='store', type=int, default=1024, help='length of RSA keys in bits (default: 1024')

cli_args = cli_parser.parse_args()

if cli_args.create_keys:
    create_new_RSA_keys(cli_args.key_length)