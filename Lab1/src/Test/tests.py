
from unittest import TestCase

from CryptoSystems.CryptoWrapper import CryptoWrapper

class CryptoTest(TestCase):
    def test_Caesar(self):
        crypter = CryptoWrapper(method = 'Caesar',
                                key_path = './Data/key_Cipher.txt' ,
                                do_encrypt = 'enc')

        with open('./Data/in.txt', 'r') as f:
            decript_data = f.readline()
        # end with

        crypter.encrypt()

        encript_data = CryptoWrapper(method = 'Caesar', 
                                     key_path = './Data/key_Cipher.txt',
                                     input_path = './Data/crypt.txt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Affine(self):
        crypter = CryptoWrapper(method = 'Affine',
                                key_path = './Data/key_Affine.txt' ,
                                do_encrypt = 'enc')

        with open('./Data/in.txt', 'r') as f:
            decript_data = f.readline()
        # end with

        crypter.encrypt()

        encript_data = CryptoWrapper(method = 'Affine', 
                                     key_path = './Data/key_Affine.txt',
                                     input_path = './Data/crypt.txt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Replace(self):
        crypter = CryptoWrapper(method = 'Replace',
                                key_path = './Data/key_Replace.txt' ,
                                do_encrypt = 'enc')
        
        with open('./Data/in.txt', 'r') as f:
            decript_data = f.readline()
        # end with

        crypter.encrypt()

        encript_data = CryptoWrapper(method = 'Replace', 
                                     key_path = './Data/key_Replace.txt',
                                     input_path = './Data/crypt.txt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Hill(self):
        crypter = CryptoWrapper(method = 'Hill',
                                key_path = './Data/key_Hill.txt' ,
                                do_encrypt = 'enc')
        
        with open('./Data/in.txt', 'r') as f:
            decript_data = f.readline()
        # end with

        crypter.encrypt()

        encript_data = CryptoWrapper(method = 'Hill', 
                                     key_path = './Data/key_Hill.txt',
                                     input_path = './Data/crypt.txt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Permutation(self):
        crypter = CryptoWrapper(method = 'Permutation',
                                key_path = './Data/key_Permutation.txt' ,
                                do_encrypt = 'enc')

        with open('./Data/in.txt', 'r') as f:
            decript_data = f.readline()
        # end with

        crypter.encrypt()

        encript_data = CryptoWrapper(method = 'Permutation', 
                                     key_path = './Data/key_Permutation.txt',
                                     input_path = './Data/crypt.txt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def

    def test_Vigenere(self):
        crypter = CryptoWrapper(method = 'Vigenere',
                                key_path = './Data/key_Vigenere.txt' ,
                                do_encrypt = 'enc')
        
        with open('./Data/in.txt', 'r') as f:
            decript_data = f.readline()
        # end with

        crypter.encrypt()

        encript_data = CryptoWrapper(method = 'Vigenere', 
                                     key_path = './Data/key_Vigenere.txt',
                                     input_path = './Data/crypt.txt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def
# end class
