
from CryptoSystems.CaesarCipher import CaesarCipher
from CryptoSystems.AffineCipher import AffineCipher
from CryptoSystems.ReplaceCipher import ReplaceCipher
from CryptoSystems.HillChipher import HillCipher

class CryptoWrapper(object):
    def __init__(self,
                 method : str,
                 key_path : str,
                 do_encrypt : str,
                 alphabet_path : str = './Data/alphabet.txt',
                 input_path : str = './Data/in.txt',
                 output_path : str = None) -> None:
        
        match method:
            case 'Caesar':
                self.crypter = CaesarCipher(alphabet_path = alphabet_path,
                                            input_path = input_path,
                                            key_path = key_path,
                                            do_encrypt = do_encrypt,
                                            output_path = output_path)
            # end case
            case 'Affine':
                self.crypter = AffineCipher(alphabet_path = alphabet_path,
                                            input_path = input_path,
                                            key_path = key_path,
                                            do_encrypt = do_encrypt,
                                            output_path = output_path)
            # end case
            case 'Replace':
                self.crypter = ReplaceCipher(alphabet_path = alphabet_path,
                                            input_path = input_path,
                                            key_path = key_path,
                                            do_encrypt = do_encrypt,
                                            output_path = output_path)
            # end case
            case 'Hill':
                self.crypter = HillCipher(alphabet_path = alphabet_path,
                                            input_path = input_path,
                                            key_path = key_path,
                                            do_encrypt = do_encrypt,
                                            output_path = output_path)
            # end case
        # end math
    # end def 

    def encrypt(self) -> str:
        return self.crypter.encrypt()
    # end def
# end class
