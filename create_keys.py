import algorithms
from secrets import randbelow,randbits

def create_prime_number(prime_number_length):
    while True:
        prime_candidate = randbits(prime_number_length)
        if algorithms.Miller_Rabin_test(prime_candidate,11):
            return prime_candidate

#kovakoodattu nyt, myöhemmin komentoriviargumenttina
key_length = 1024

p = create_prime_number(key_length // 2)
q = create_prime_number(key_length // 2)

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

#Constructing secret key exponent d
#Requires Extended Euclidean algorithm
#while True:
    #d_candidate = randbelow(N)
    #if (d_candidate * e - 1) % N_ == 0:
        #break
#d = d_candidate

print(f'N: {N}, N_: {N_}, e: {e}, d: kytketty pois')