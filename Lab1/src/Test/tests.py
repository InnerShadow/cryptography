
from unittest import TestCase

from CryptoSystems.CryptoWrapper import CryptoWrapper

class CryptoTest(TestCase):
    def test_Caesar(self):
        crypter = CryptoWrapper(method = 'Caesar',
                                key_path = './Data/key_Cipher.txt' ,
                                do_encrypt = 'enc')
        crypter.encrypt()
        decript_data = crypter.crypter.input_str
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
        crypter.encrypt()
        decript_data = crypter.crypter.input_str
        encript_data = CryptoWrapper(method = 'Affine', 
                                     key_path = './Data/key_Affine.txt',
                                     input_path = './Data/crypt.txt',
                                     do_encrypt = 'dec').encrypt()
        self.assertEqual(decript_data, encript_data)
    # end def
# end class