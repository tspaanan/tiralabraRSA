import math
from secrets import randbelow

#Euclidean algorithm checks the Greatest Common Divisor of two integers
def Euclidean_algorithm(larger_int, smaller_int):
    result = -1
    while result != 0:
        temp_int = larger_int // smaller_int
        result = larger_int - smaller_int * temp_int
        larger_int = smaller_int
        smaller_int = result

    #GCD is the last result that was not zero
    return larger_int

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
        print('false1')
        return False
#bound-and-branch testi tähän
    previous_even = prime_candidate - 1
    #factoring out powers of 2
    #puolita, kunnes jakojäännös ei enää ole nolla, ota edellinen tulos
    #se on d, jolloin s on candidate / d
    d, s = _factoring_out_powers_of_2(previous_even)
    for _ in range(nbr_of_rounds):
        str_base_candidate = 1
        while str_base_candidate < 2:
            str_base_candidate = randbelow(previous_even)
        #x = str_base_candidate ** d % prime_candidate
        x = pow(str_base_candidate, d, prime_candidate)
        for _ in range(s):
            y = x ** 2 % prime_candidate
            if y == 1 and x != 1 and x != previous_even:
                print('false2')
                return False
            x = y
        if y != 1:
            print('false3')
            return False
    return True
#https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test