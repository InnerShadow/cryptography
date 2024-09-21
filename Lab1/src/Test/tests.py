
from unittest import TestCase

from CryptoSystems.CryptoWrapper import CryptoWrapper

class CryptoTest(TestCase):
    def test_Caesar(self):
        crypter = CryptoWrapper(method = 'Caesar',
                                key_path = './Data/key_Caesar' ,
                                do_encrypt = 'enc').encrypt()

        with open('./Data/in', 'r') as f:
            decript_data = f.readline()
        # end with

        encript_data = CryptoWrapper(method = 'Caesar', 
                                     key_path = './Data/key_Caesar',
                                     input_path = './Data/crypt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Affine(self):
        crypter = CryptoWrapper(method = 'Affine',
                                key_path = './Data/key_Affine' ,
                                do_encrypt = 'enc').encrypt()

        with open('./Data/in', 'r') as f:
            decript_data = f.readline()
        # end with

        encript_data = CryptoWrapper(method = 'Affine', 
                                     key_path = './Data/key_Affine',
                                     input_path = './Data/crypt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Replace(self):
        crypter = CryptoWrapper(method = 'Replace',
                                key_path = './Data/key_Replace' ,
                                do_encrypt = 'enc').encrypt()
        
        with open('./Data/in', 'r') as f:
            decript_data = f.readline()
        # end with

        encript_data = CryptoWrapper(method = 'Replace', 
                                     key_path = './Data/key_Replace',
                                     input_path = './Data/crypt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Hill(self):
        crypter = CryptoWrapper(method = 'Hill',
                                key_path = './Data/key_Hill' ,
                                do_encrypt = 'enc').encrypt()
        
        with open('./Data/in', 'r') as f:
            decript_data = f.readline()
        # end with

        encript_data = CryptoWrapper(method = 'Hill', 
                                     key_path = './Data/key_Hill',
                                     input_path = './Data/crypt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Permutation(self):
        crypter = CryptoWrapper(method = 'Permutation',
                                key_path = './Data/key_Permutation' ,
                                do_encrypt = 'enc').encrypt()

        with open('./Data/in', 'r') as f:
            decript_data = f.readline()
        # end with

        encript_data = CryptoWrapper(method = 'Permutation', 
                                     key_path = './Data/key_Permutation',
                                     input_path = './Data/crypt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Vigenere(self):
        crypter = CryptoWrapper(method = 'Vigenere',
                                key_path = './Data/key_Vigenere' ,
                                do_encrypt = 'enc').encrypt()
        
        with open('./Data/in', 'r') as f:
            decript_data = f.readline()
        # end with

        encript_data = CryptoWrapper(method = 'Vigenere', 
                                     key_path = './Data/key_Vigenere',
                                     input_path = './Data/crypt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def
# end class
