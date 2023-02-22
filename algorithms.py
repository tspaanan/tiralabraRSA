from math import isqrt
from secrets import randbelow

#Euclidean algorithm calculates the Greatest Common Divisor of two integers
def Euclidean_algorithm(larger_int, smaller_int):
    result = -1
    while result != 0:
        temp_int = larger_int // smaller_int
        result = larger_int - smaller_int * temp_int
        larger_int = smaller_int
        smaller_int = result

    #GCD is the last result that was not zero
    return larger_int

#Euclidean extended algorithm calculates the Greatest Common Divisor of two integers
#and Bézout coefficients
def Extended_Euclidean_algorithm(larger_int, smaller_int):
    result = -1
    bco_s1, bco_s2 = 0, 1
    bco_t1, bco_t2 = 1, 0
    while result != 0:
        temp_int = larger_int // smaller_int
        result = larger_int - smaller_int * temp_int
        bco_stmp = bco_s2 - bco_s1 * temp_int
        bco_ttmp = bco_t2 - bco_t1 * temp_int
        larger_int = smaller_int
        smaller_int = result
        bco_s2 = bco_s1
        bco_s1 = bco_stmp
        bco_t2 = bco_t1
        bco_t1 = bco_ttmp

    #GCD and Bézout coefficients are the last results where GCD was not zero
    return (larger_int, bco_s2, bco_t2)

def _factoring_out_powers_of_2(base_integer):
    halved_integer = base_integer // 2
    while halved_integer % 2 == 0:
        halved_integer = halved_integer // 2
    return (halved_integer, base_integer // halved_integer)

#Miller-Rabin test finds out if an integer is a prime number with high probability
#Implementation follows the principles in Cormen, Thomas H.; Leiserson, Charles E.;
#Rivest, Ronald L.; Stein, Clifford (2009) [1990]. "31". Introduction to Algorithms
# (3rd ed.). MIT Press and McGraw-Hill. pp. 968–971
def Miller_Rabin_test(prime_candidate, nbr_of_rounds):
    if prime_candidate in [2,3]:
        return True
    if prime_candidate < 2 or prime_candidate % 2 == 0:
        return False
    
    #pruning prime_candidates before Miller-Rabin test
    with open('prime_numbers','r') as file_object:
        list_of_primes = [int(line.strip()) for line in file_object]
        for prime in list_of_primes[:500]:
            if prime > isqrt(prime_candidate):
                break
            if prime_candidate % prime == 0:
                return False
    
    previous_even = prime_candidate - 1
    
    d, s = _factoring_out_powers_of_2(previous_even)

    for _ in range(nbr_of_rounds):
        str_base_candidate = 1
        while str_base_candidate < 2:
            str_base_candidate = randbelow(previous_even)
        x = pow(str_base_candidate, d, prime_candidate)
        for _ in range(s):
            y = pow(x, 2, prime_candidate)
            if y == 1 and x != 1 and x != previous_even:
                return False
            x = y
        if y != 1:
            return False
    return True