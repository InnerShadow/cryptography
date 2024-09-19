
from abc import ABC, abstractmethod

class CryptographySystem(ABC):
    def __init__(self, 
                 alphabet_path : str,
                 input_path : str,
                 key_path : str,
                 do_encrypt : str,
                 output_path : str = None) -> None:
        
        ouput_map = {
            'enc' : './Data/crypt.txt',
            'dec' : './Data/decrypt.txt'
        }
        
        self.output_path = ouput_map[do_encrypt] if not output_path else output_path
        
        encrypt_map = {
            'enc' : self._encrypt_single_character,
            'dec' : self._decrypt_single_character
        }
        
        self.encrypt_function = encrypt_map[do_encrypt]
        
        with open(alphabet_path, 'r') as f:
            self.alphabet = f.readline().strip()
        # end with

        self.M = len(self.alphabet)

        with open(input_path, 'r') as f:
            self.input_str = f.readline().strip()
        # end with
        
        with open(key_path, 'r') as f:
            self.key = f.readline().strip()
        # end with

        if not set(self.input_str).issubset(set(self.alphabet)):
            raise ValueError('Bad input string.')
        # end if

        if not set(self.key).issubset(set(self.alphabet)):
            raise ValueError('Bad key.')
        # end if

        self._check_key()
        self._preprocess_key()
    # end def

    @abstractmethod
    def _check_key(self):
        raise NotImplementedError()

    @abstractmethod
    def _preprocess_key(self) -> None:
        raise NotImplementedError()
    # end def

    @abstractmethod
    def _encrypt_single_character(self, symbol : str) -> str:
        raise NotImplementedError()
    # end def

    @abstractmethod
    def _decrypt_single_character(self, symbol : str) -> str:
        raise NotImplementedError()
    # end def

    def encrypt(self) -> str:
        res = ''

        for i in self.input_str:
            res += self.encrypt_function(i)
        # end for

        self._write_ouput(res)

        return res
    # end def

    def _write_ouput(self, data : str):
        with open(self.output_path, 'w') as f:
            f.write(data)
        # end with
    # end def
# end class
