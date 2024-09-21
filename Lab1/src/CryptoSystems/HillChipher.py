
import numpy as np

from CryptoSystems.CryptographySystem import CryptographySystem

MATRIX_SHAPE = 2


class HillCipher(CryptographySystem):

    def __init__(self, 
                 alphabet_path: str, 
                 input_path: str, 
                 key_path: str, 
                 do_encrypt: str, 
                 output_path: str = None) -> None:
        super().__init__(alphabet_path = alphabet_path, 
                         input_path = input_path, 
                         key_path = key_path, 
                         do_encrypt = do_encrypt, 
                         output_path = output_path)
        
        self._do_add_enc_character = False
        
        if len(self.input_str) % MATRIX_SHAPE != 0:
            self.input_str += self.alphabet[-1]
            self._do_add_enc_character = True
        # end if
    # end def

    def _preprocess_key(self) -> None:
        self.key_matrix = np.array([[self.alphabet.index(self.key[0]), self.alphabet.index(self.key[1])], 
                                    [self.alphabet.index(self.key[2]), self.alphabet.index(self.key[3])]])

        det = int(np.round(np.linalg.det(self.key_matrix)))
        
        det_inv = pow(det, -1, self.M)

        adjugate_matrix = np.array([[self.key_matrix[1, 1], -self.key_matrix[0, 1]], 
                                    [-self.key_matrix[1, 0], self.key_matrix[0, 0]]])
        self.key_matrix_inv = (det_inv * adjugate_matrix) % self.M
    # end def

    def _check_key(self) -> None:
        if len(self.key) != 4:
            raise ValueError('Bad key.')
        # end if

        key_matrix = np.array([[self.alphabet.index(self.key[0]), self.alphabet.index(self.key[1])], 
                           [self.alphabet.index(self.key[2]), self.alphabet.index(self.key[3])]])

        det = int(np.round(np.linalg.det(key_matrix)))

        if det == 0:
            raise ValueError('Bad key.')
        # end if

        try:
            det_inv = pow(det, -1, self.M)
        except ValueError:
            raise ValueError(f'Bad key.')
        # end try
    # end def
    
    def encrypt(self) -> str:
        res = ''

        for i in range(0, len(self.input_str), MATRIX_SHAPE):
            res += self.encrypt_function(self.input_str[i:i+MATRIX_SHAPE])
        # end for

        # res = res if not self._do_add_enc_character else res[:-1]

        self._write_output(res)

        return res
    # end def

    def _encrypt_single_character(self, symbol : str) -> str:
        symbol = np.array([self.alphabet.index(symbol[0]), self.alphabet.index(symbol[1])])

        symbol = np.dot(self.key_matrix, symbol) % self.M

        return ''.join(self.alphabet[i] for i in symbol)
    # end def

    def _decrypt_single_character(self, symbol : str) -> str:
        symbol = np.array([self.alphabet.index(symbol[0]), self.alphabet.index(symbol[1])])

        symbol = np.dot(self.key_matrix_inv, symbol) % self.M

        return ''.join(self.alphabet[int(i)] for i in symbol)
    # end def
# end class
