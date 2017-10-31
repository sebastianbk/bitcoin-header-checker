import hashlib, sys


if __name__ == '__main__':
    header_hex = sys.argv[1]
    header_bin = header_hex.decode('hex')
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    print(hash[::-1].encode('hex_codec'))
