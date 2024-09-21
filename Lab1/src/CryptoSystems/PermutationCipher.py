from CryptoSystems.CryptographySystem import CryptographySystem

MAX_TMP_FILL = 35

class PermutationCipher(CryptographySystem):
    def _check_key(self) -> None:
        if len(set(self.key)) != len(self.key) or len(self.key) > self.M:
            raise ValueError('Bad key.')
        # end if
    # end def

    def _preprocess_key(self) -> None:
        key_indices = [self.alphabet.index(k) for k in self.key]
        self.key_indices = [MAX_TMP_FILL] * len(self.key)
        for i in range(len(self.key)):
            self.key_indices[key_indices.index(min(key_indices))] = i
            key_indices[key_indices.index(min(key_indices))] = MAX_TMP_FILL
        # end for
    # end def

    def _encrypt_single_character(self, symbol : str) -> str:
        outout_str = ''
        for i in self.key_indices:
            outout_str += symbol[i]
        # end for

        return outout_str
    # end def

    def _decrypt_single_character(self, symbol: str) -> str:
        return self._encrypt_single_character(symbol)
    # end def

    def encrypt(self) -> str:
        num_padded_chars = 0
        while len(self.input_str) % len(self.key) != 0:
            num_padded_chars += 1
            self.input_str += self.alphabet[-1]
        # end while

        res = ''

        for i in range(0, len(self.input_str), len(self.key)):
            res += self.encrypt_function(self.input_str[i:i+len(self.key)])
        # end for

        res = res if not num_padded_chars else res[:-num_padded_chars]
        
        self._write_output(res)
        return res
    # end def
# end class
