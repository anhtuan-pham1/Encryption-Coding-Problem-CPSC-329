import unittest
import caesarDecrypt

class TestCaesar(unittest.TestCase):
    
    def test_cipherText(self):
        #Tests different ciphertexts with the same key and shift
        key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        shift = -10

        #Test Cases
        fullSentence = "Fb40i4 2edj8dk4 je fh02j824 fhef4h ie280b 38ij0d28d6"
        emptyString = ""
        specialCharacters = "!@#$%^&*()?><:" 
        allCharactersInKey = "jzKEab0IMNLQl18CAkiPx7SpTgswRUX6fq3oW5hJFeyn4HruBODmZctGv2dVY9"

        #Tests
        self.assertEqual(caesarDecrypt.caesarDecrypt(key, fullSentence, shift), "Please continue to practice proper social distancing")
        self.assertEqual(caesarDecrypt.caesarDecrypt(key, emptyString, shift), "")
        self.assertEqual(caesarDecrypt.caesarDecrypt(key, specialCharacters, shift), specialCharacters) #No change because special characters not in key
        self.assertEqual(caesarDecrypt.caesarDecrypt(key, allCharactersInKey, shift), "tJUOklaSWXV0vbiMKusZHh2z3qCG147gpAdy6frTPoIxeRBELYNw9mDQFcn58j")

    def test_shift(self):
        #Tests different shifts with same ciphertext and key
        key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        #Test Cases
        fullSentence = "Fb40i4 2edj8dk4 je fh02j824 fhef4h ie280b 38ij0d28d6"

        self.assertEqual(caesarDecrypt.caesarDecrypt(key, fullSentence, -10), "Please continue to practice proper social distancing")
        self.assertEqual(caesarDecrypt.caesarDecrypt(key, fullSentence, 0), "Fb40i4 2edj8dk4 je fh02j824 fhef4h ie280b 38ij0d28d6")
        self.assertEqual(caesarDecrypt.caesarDecrypt(key, fullSentence, 10), "v1UQ8U S439Y3aU 94 57QS9YSU 5745U7 84SYQ1 TY89Q3SY3W")
    
    def test_key(self):
        #Tests different keys with same ciphertext and shift
        fullSentence = "Fb40i4 2edj8dk4 je fh02j824 fhef4h ie280b 38ij0d28d6"
        shift = -10

        #Test Cases
        key1 = 'abcdefghijklmnopqrstuvwxyz'
        key2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key3 = '0123456789'
        
        

        self.assertEqual(caesarDecrypt.caesarDecrypt(key1, fullSentence, shift), "Fl40s4 2ont8nu4 to pr02t824 prop4r so280l 38st0n28n6")
        self.assertEqual(caesarDecrypt.caesarDecrypt(key2, fullSentence, shift), "Pb40i4 2edj8dk4 je fh02j824 fhef4h ie280b 38ij0d28d6")
        self.assertEqual(caesarDecrypt.caesarDecrypt(key3, fullSentence, shift), "Fb40i4 2edj8dk4 je fh02j824 fhef4h ie280b 38ij0d28d6")


#Allows test to be called directly from command line
if __name__ == '__main__':
    unittest.main()

    
