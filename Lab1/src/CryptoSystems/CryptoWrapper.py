
from CryptoSystems.CaesarCipher import CaesarCipher

class CryptoWrapper(object):
    def __init__(self,
                 method : str,
                 alphabet_path : str,
                 input_path : str,
                 key_path : str,
                 do_encrypt : str,
                 output_path : str = None) -> None:
        
        match method:
            case 'Caesar':
                self.cryptho = CaesarCipher(alphabet_path = alphabet_path,
                                            input_path = input_path,
                                            key_path = key_path,
                                            do_encrypt = do_encrypt,
                                            output_path = output_path)
            # end case
        # end math
    # end def 

    def encrypt(self) -> str:
        return self.cryptho.encrypt()
    # end def
# end class