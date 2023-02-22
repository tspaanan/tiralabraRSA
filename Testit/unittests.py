import unittest
import algorithms
import create_keys
import encryptions
import key_objects
import message_objects
import secrets
import string

class TestAlgorithms(unittest.TestCase):

    def test_Euclidean_algorithm(self):
        self.assertEqual(algorithms.Euclidean_algorithm(408,112), 8)
        self.assertNotEqual(algorithms.Euclidean_algorithm(408,112), 11)
        self.assertEqual(algorithms.Euclidean_algorithm(25,15), 5)
        self.assertNotEqual(algorithms.Euclidean_algorithm(25,15), 13)

    def test_Extended_Euclidean_algorithm(self):
        self.assertEqual(algorithms.Extended_Euclidean_algorithm(20,3),(1,-1,7))
        self.assertNotEqual(algorithms.Extended_Euclidean_algorithm(20,3),(1,1,-6))
        self.assertEqual(algorithms.Extended_Euclidean_algorithm(4864,3458),(38,32,-45))
        self.assertNotEqual(algorithms.Extended_Euclidean_algorithm(4864,3458),(39,31,-44))

    def test__factoring_out_powers_of_2(self):
        self.assertEqual(algorithms._factoring_out_powers_of_2(220), (55,4))
        self.assertNotEqual(algorithms._factoring_out_powers_of_2(220), (54,6))

    def test_Miller_Rabin_test(self):
        self.assertTrue(algorithms.Miller_Rabin_test(19997,40))
        self.assertFalse(algorithms.Miller_Rabin_test(19995,40))
        self.assertTrue(algorithms.Miller_Rabin_test(541,40))
        self.assertFalse(algorithms.Miller_Rabin_test(539,40))
        
    def test_Miller_Rabin_test_with_large_integers(self):
        #Using Bell primes for large prime numbers
        self.assertTrue(algorithms.Miller_Rabin_test(35742549198872617291353508656626642567,40))
        self.assertFalse(algorithms.Miller_Rabin_test(35742549198872617291353508656626642565,40))
        self.assertTrue(algorithms.Miller_Rabin_test(359334085968622831041960188598043661065388726959079837,40))
        self.assertFalse(algorithms.Miller_Rabin_test(359334085968622831041960188598043661065388726959079835,40))

class TestEncryptions(unittest.TestCase):

    def setUp(self):
        #Setting up 1024-bit RSA key pair, message length restricted to 127 bytes (for safe margin)
        self.keys_for_testing = create_keys.create_new_RSA_keys(1024)
        self.message_for_testing = ''.join(secrets.choice(string.ascii_letters) for _ in range(127))
        self.encrypted_message_for_testing = encryptions.encrypt_message(message_objects.Message(self.message_for_testing,False),self.keys_for_testing[0])

    def test_first_encrypt_message(self):
        self.assertTrue(self.encrypted_message_for_testing.encrypted)

    def test_second_decrypt_message(self):
        self.decrypted_message_for_testing = encryptions.decrypt_message(self.encrypted_message_for_testing,self.keys_for_testing[1])
        self.assertFalse(self.decrypted_message_for_testing.encrypted)
        self.assertEqual(self.decrypted_message_for_testing.message_content,self.message_for_testing)

class TestKeyCreation(unittest.TestCase):

    #Creating random prime number, length 14 bits
    #List contains the first 2,262 prime numbers for assertion
    def test_prime_number_creation(self):
        with open('prime_numbers', 'r') as file_object:
            list_of_primes = [int(line.strip()) for line in file_object]
        self.assertIn(create_keys._create_prime_number(14),list_of_primes)
    
    def test_key_creation(self):
        key_pair = create_keys.create_new_RSA_keys(1024)
        self.assertEqual(key_pair[0].modulus_n,key_pair[1].modulus_n)
        self.assertEqual(key_pair[0].keyclass,key_objects.KeyClass.SECRET)
        self.assertEqual(key_pair[1].keyclass,key_objects.KeyClass.PUBLIC)
        self.assertNotEqual(key_pair[0].exponent,key_pair[1].exponent)

if __name__ == '__main__':
    unittest.main()