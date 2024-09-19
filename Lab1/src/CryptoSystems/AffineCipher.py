
from math import gcd

from CryptoSystems.CryptographySystem import CryptographySystem

class AffineCipher(CryptographySystem):

    def _mod_inverse(self) -> int:
        for x in range(1, self.M):
            if (self.key_k1 * x) % self.M == 1:
                return x
            # end if
        # end for
        raise ValueError('Bad key.')
    # end def

    def _preprocess_key(self) -> None:
        self.key_k1 = self.alphabet.index(self.key[0])
        self.key_k2 = self.alphabet.index(self.key[1])

        self._check_k1()

        self.key_k1_inverse = self._mod_inverse()
    # end def

    def _check_k1(self) -> None:
        if gcd(self.key_k1, self.M) != 1:
            raise ValueError('Bad key.')
        # end if
    # end def

    def _check_key(self) -> None:
        if len(self.key) != 2:
            raise ValueError('Bad key.')
        # end if
    # end def

    def _encrypt_single_character(self, symbol : str) -> str:
        return self.alphabet[(self.key_k1 * self.alphabet.index(symbol) + self.key_k2) % self.M]
    # end def

    def _decrypt_single_character(self, symbol : str) -> str:
        return self.alphabet[(self.key_k1_inverse * (self.alphabet.index(symbol) - self.key_k2)) % self.M]
    # end def
# end class
