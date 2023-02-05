import algorithms
import key_objects
from secrets import randbelow,randbits

def _create_prime_number(prime_number_length):
    while True:
        prime_candidate = randbits(prime_number_length)
        if algorithms.Miller_Rabin_test(prime_candidate,11):
            return prime_candidate

def create_new_RSA_keys(key_length):
    while True:
        p = _create_prime_number(key_length // 2)
        q = _create_prime_number(key_length // 2)

        N = p * q
        N_ = (p-1) * (q-1)

        #Constructing public key exponent e that is coprime for N_
        gcd = 0
        while gcd != 1:
            e_candidate = 1
            while e_candidate < 2:
                e_candidate = randbelow(N_)
            gcd = algorithms.Euclidean_algorithm(N_, e_candidate)
        e = e_candidate

        #Constructing secret key exponent d that is modular multiplicative inversion of e mod N_
        #Secret key exponent d has to be a positive integer
        d_candidate = algorithms.Extended_Euclidean_algorithm(N_,e)[2]
        if d_candidate > 0:
            d = d_candidate
            break

    print(f'N: {N}, N_: {N_}, e: {e}, d: {d}')
    secret_key = key_objects.SecretKey(N,d)
    print(f'Created {secret_key}')
    public_key = key_objects.PublicKey(N,e)
    print(f'Created {public_key}')