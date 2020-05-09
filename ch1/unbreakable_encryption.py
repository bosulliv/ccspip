# -*- coding: utf-8 -*-
""" One time pad encryption decryption """
from secrets import token_bytes
from typing import Tuple

def random_keys(length: int) -> int:
    """: generate length random bytes """
    tokeb: bytes = token_bytes(length)
    # convert to string
    return int.from_bytes(tokeb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    """ encrypt message with random key. return both """
    # Turn string into stream of bytes
    original_bytes: bytes = original.encode()
    # Create our random key which will be the same length
    dummy: int = random_keys(len(original_bytes))
    # Turn our byte string into a large integer
    original_key: int = int.from_bytes(original_bytes, "big")
    # XOR string int and key int to encrypt
    encrypted: int = original_key ^ dummy
    # Return our key and the encrypted message
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    """ decrypt message with key """
    decrypted: int = key1 ^ key2
    # If we have 00000001 as the most significant byte
    # Integer division would round d
    msg_len = (decrypted.bit_length()+7)// 8
    # Turn the encrypted into a sequence of bytes
    temp: bytes = decrypted.to_bytes(msg_len, "big")
    # return the bytes decoded into a string
    return temp.decode()

if __name__ == '__main__':
    k1, k2 = encrypt("One Time Pad!")
    result: str = decrypt(k1, k2)
    print(result)
