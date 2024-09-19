
from CryptoSystems.CryptographySystem import CryptographySystem

class CaesarCipher(CryptographySystem):
    def _check_key(self) -> None:
        if len(self.key) != 1:
            raise ValueError('Bad key.')
        # end if
    # end def

    def _encrypt_single_character(self, symbol : str) -> str:
        return self.alphabet[(self.alphabet.index(symbol) + self.key) % self.M]
    # end def

    def _decrypt_single_character(self, symbol : str) -> str:
        return self.alphabet[(self.alphabet.index(symbol) - self.key) % self.M]
    # end def

    def _preprocess_key(self) -> None:
        self.key = self.alphabet.index(self.key)
    # end def
# end class
