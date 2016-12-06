"""This is a encoding program."""
# coding = UTF-8

import hashlib
import base64
import sys

def calc_hash(mystring):
    u'''入力文字列のハッシュ値を求めて辞書型で出力する'''
    make_hash_dict = {
        'md5': hashlib.md5(mystring).hexdigest(),
        'sha1': hashlib.sha1(mystring).hexdigest(),
        'sha224': hashlib.sha224(mystring).hexdigest(),
        'sha256': hashlib.sha256(mystring).hexdigest(),
        'sha384': hashlib.sha384(mystring).hexdigest(),
        'sha512': hashlib.sha512(mystring).hexdigest(),
        'a85': base64.a85encode(mystring),
        'sb64': base64.standard_b64encode(mystring),
        'ub64': base64.urlsafe_b64encode(mystring),
        'b16': base64.b16encode(mystring),
        'b32': base64.b32encode(mystring),
        'b64': base64.b64encode(mystring),
        'b85': base64.b85encode(mystring),
    }
    return make_hash_dict

if __name__ == '__main__':
    MY_STRING = sys.argv[0]
    MY_STRING = "take to you"
    HASH_DICT = calc_hash(MY_STRING.encode())
    for key, value in HASH_DICT.items():
        print('{0}\t{1}'.format(key, value))
    print(MY_STRING)
