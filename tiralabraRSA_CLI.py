import argparse

# https://docs.python.org/3/library/argparse.html

cli_parser = argparse.ArgumentParser(description='CLI for tiralabraRSA: create RSA keys, encrypt and decrypt messages')

cli_parser.add_argument('--create_keys', action='store_true', help='create new RSA keys with variable length')

cli_args = cli_parser.parse_args()

if cli_args.create_keys:
    #print('toimii')
    #testataan alkulukujen validointia M-R testillä
    import algorithms
    alkuluvut = []
    for i in range(20000):
        print(i)
        if algorithms.Miller_Rabin_test(i,11):
            alkuluvut.append(i)
    print(len(alkuluvut))

print('loppu')