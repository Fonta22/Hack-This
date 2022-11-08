import sys
import binascii

try:
    print(bytes.fromhex(sys.argv[1]).decode('utf-8'))
except:
    print(binascii.hexlify(bytes(sys.argv[1], 'utf-8')).decode('utf-8').upper())