from CryptoSystems.CryptographySystem import CryptographySystem

class VigenereCipher(CryptographySystem):
    def _check_key(self) -> None:
        pass
    # end def

    def _preprocess_key(self) -> None:
        self.key_indices = [self.alphabet.index(k) for k in self.key]
    # end def

    def _encrypt_single_character(self, symbol: str, position: int) -> str:
        key_pos = position % len(self.key)
        shift = self.key_indices[key_pos]
        return self.alphabet[(self.alphabet.index(symbol) + shift) % self.M]
    # end def

    def _decrypt_single_character(self, symbol: str, position: int) -> str:
        key_pos = position % len(self.key)
        shift = self.key_indices[key_pos]
        return self.alphabet[(self.alphabet.index(symbol) - shift) % self.M]
    # end def

    def encrypt(self) -> str:
        res = ''.join(self.encrypt_function(char, i) for i, char in enumerate(self.input_str))
        
        self._write_output(res)
        return res
    # end def
# end class
