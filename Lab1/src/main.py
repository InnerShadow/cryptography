import argparse
from CryptoSystems.CryptoWrapper import CryptoWrapper

def main():
    parser = argparse.ArgumentParser(description = "Cryptography System Wrapper")

    parser.add_argument('method', type = str, help = "(Caesar, Affine, Replace, Hill, Permutation, Vigenere)")
    parser.add_argument('do_encrypt', type = str, choices = ['enc', 'dec'])

    parser.add_argument('--alphabet_path', type = str, default = './Data/alphabet')
    parser.add_argument('--input_path', type = str, default = './Data/in')
    parser.add_argument('--key_path', type = str)
    parser.add_argument('--output_path', type = str)
    
    args = parser.parse_args()

    if args.key_path is None:
        args.key_path = f'./Data/key_{args.method}'
    # end if 

    crypto = CryptoWrapper(
        method = args.method,
        alphabet_path = args.alphabet_path,
        input_path = args.input_path,
        key_path = args.key_path,
        do_encrypt = args.do_encrypt,
        output_path = args.output_path
    )

    result = crypto.encrypt()
    print(result)
# end def

if __name__ == '__main__':
    main()
# end if
