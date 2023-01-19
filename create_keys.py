from secrets import randbelow

with open('prime_numbers', 'r') as file_object:
    list_of_primes = [line.strip() for line in file_object]

print(len(list_of_primes))

p = q = randbelow(len(list_of_primes))
while p == q:
    q = randbelow(len(list_of_primes))

print(p)
print(q)

N = p * q
print(N)

N_ = (p-1) * (q-1)
print(N_)

#selvitetään alkuluvun suhteellisuus
def check_GCD(e_max, e_min): #check Greatest Common Divisor
    result = -1
    while result != 0:
        #print(f'{e_max} {e_min} {result}')
        e_temp = e_max // e_min
        result = e_max - e_min * e_temp
        e_max = e_min
        e_min = result
    #viimeisin nollasta poikkeava on yhteinen tekijä
    return(e_max)

gcd = 0
while gcd != 1:
    e_candidate = 1
    while e_candidate < 2:
        e_candidate = randbelow(N_)
    print(e_candidate)
    gcd = check_GCD(N_, e_candidate)
    if gcd != 1:
        print(f'ei kelpaa: {e_candidate}')
print(f'löytyi e: {e_candidate}')

#e_max = N_
#e_min = e_candidate

#print(check_GCD(7,5))

e = e_candidate

#viimein etsitään luku d
while True:
    d_candidate = randbelow(N)
    print(d_candidate)
    if (d_candidate * e - 1) % N_ == 0:
        break
    print(f'ei kelpaa: {d_candidate}')
print(f'löytyi d: {d_candidate}')

d = d_candidate

print(f'N: {N}, N_: {N_}, e: {e}, d: {d}')