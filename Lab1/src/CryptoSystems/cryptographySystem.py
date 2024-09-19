
from abc import ABC, abstractmethod

class cryptographySystem(ABC):
    def __init__(self, 
                 alphabet_path : str,
                 input_path : str,
                 key_path : str,
                 do_encrypt : str) -> None:
        
        encrypt_map = {
            'enc' : self._encrypt_single_character,
            'dec' : self._decrypt_single_character
        }
        
        self.encrypt_function = encrypt_map[do_encrypt]
        
        with open(alphabet_path, 'r') as f:
            self.alphabet = f.readline()
        # end with

        self.M = len(self.alphabet)

        with open(input_path, 'r') as f:
            self.input_str = f.readline()
        # end with
        
        with open(key_path, 'r') as f:
            self.key = f.readline()
        # end with

        if not set(self.input_str).issubset(set(self.alphabet)):
            raise ValueError('Bad input string.')
        # end if

        if not set(self.key).issubset(set(self.alphabet)):
            raise ValueError('Bad key.')
        # end if
    # end def

    @abstractmethod
    def _encrypt_single_character(self) -> None:
        raise NotImplementedError()
    # end def

    @abstractmethod
    def _decrypt_single_character(self) -> None:
        raise NotImplementedError()
    # end def

    def encrypt(self) -> str:
        res = ''

        for i in self.input_str:
            res += self.encrypt_function(i)
        # end for

        return res
    # end def
# end class
