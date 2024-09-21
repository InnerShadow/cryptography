from CryptoSystems.CryptographySystem import CryptographySystem

class PermutationCipher(CryptographySystem):
    def _check_key(self) -> None:
        if len(set(self.key)) != len(self.key) or len(self.key) > self.M:
            raise ValueError('Bad key.')
        # end if
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
        padding_char = self.alphabet[0]
        num_padded_chars = 0
        while len(self.input_str) % len(self.key) != 0:
            num_padded_chars += 1
            self.input_str += padding_char
        # end while

        res = ''.join(self.encrypt_function(char, i) for i, char in enumerate(self.input_str))
        res = res if not num_padded_chars else res[:-num_padded_chars]
        
        self._write_output(res)
        return res
    # end def
# end class
