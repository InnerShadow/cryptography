
from CryptoSystems.CaesarCipher import CaesarCipher
from CryptoSystems.AffineCipher import AffineCipher
from CryptoSystems.ReplaceCipher import ReplaceCipher
from CryptoSystems.HillChipher import HillCipher
from CryptoSystems.PermutationCipher import PermutationCipher
from CryptoSystems.VigenereCipher import VigenereCipher

class CryptoWrapper(object):
    def __init__(self,
                 method : str,
                 key_path : str,
                 do_encrypt : str,
                 alphabet_path : str = './Data/alphabet.txt',
                 input_path : str = './Data/in.txt',
                 output_path : str = None) -> None:
        
        common_args = {
            'alphabet_path': alphabet_path,
            'input_path': input_path,
            'key_path': key_path,
            'do_encrypt': do_encrypt,
            'output_path': output_path
        }
        
        match method:
            case 'Caesar':
                self.crypter = CaesarCipher(**common_args)
            # end case
            case 'Affine':
                self.crypter = AffineCipher(**common_args)
            # end case
            case 'Replace':
                self.crypter = ReplaceCipher(**common_args)
            # end case
            case 'Hill':
                self.crypter = HillCipher(**common_args)
            # end case
            case 'Permutation':
                self.crypter = PermutationCipher(**common_args)
            # end case
            case 'Vigenere':
                self.crypter = VigenereCipher(**common_args)
            # end case
        # end math
    # end def 

    def encrypt(self) -> str:
        return self.crypter.encrypt().strip()
    # end def
# end class
