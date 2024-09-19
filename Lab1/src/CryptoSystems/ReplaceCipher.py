
from math import gcd

from CryptoSystems.CryptographySystem import CryptographySystem

class ReplaceCipher(CryptographySystem):

    def _preprocess_key(self) -> None:
        self.key_map = dict(zip(self.alphabet, self.key))
        self.inverse_key_map = dict(zip(self.key, self.alphabet))
    # end def

    def _check_key(self) -> None:
        if len(self.key) != self.M:
            raise ValueError('Bad key.')
        # end if
        if len(self.key) != len(set(self.key)):
            raise ValueError('Bad key.')
        # end if
    # end def

    def _encrypt_single_character(self, symbol : str) -> str:
        return self.key_map[symbol]
    # end def

    def _decrypt_single_character(self, symbol : str) -> str:
        return self.inverse_key_map[symbol]
    # end def
# end class
