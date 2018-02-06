#!/bin/python

# Standard library
from base64 import b64encode
from functools import partial
import getopt
import hashlib
import sys


# Third party library
#try:
#     import numpy
# except ImportError:
#     print("Numpy not installed")


# def main(argv):


def main():
    input_file = 'testdata/text.dat'
    compare_value = '56e713c263a07f1c2bc4c0c6f44c46d7'
    hash_value = 'md5'

    """
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["iFile=", "hValue="])
    except getopt.GetoptError("Something went wrong..."):
        help_msg('s')

    for opt, arg in opts:
        if opt == '-h':
            help_msg('l')
        elif opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-c", "--compare"):
            compare_value = arg
        elif opt in ("-h", "--hash"):
            hash_value = arg
        else:
            help_msg('l')
"""
    compare(input_file, compare_value, hash_value)


def compare(input_hash, compare_hash, tha_hash=None):
    a = hasher(input_hash, tha_hash)

    if tha_hash is None:
        if a == compare_hash:
            print("Hash is verified.")
            exit(0)
        else:
            print("Hash is not verified.")
    """elif tha_hash is not None:
        for h in a:
            if h == compare_hash:
                print("Hash is verified.")
                exit(0)
            else:
                print("Hash is not verified.")
"""

def hasher(value, mode): 
    h = ''
    if mode == "md5":
        h = hashlib.md5()
        """if mode == "md5":
            h = hashlib.md5(value)
        elif mode == "sha1":
            h = hashlib.sha1(value)
        elif mode == "sha256":
            h = hashlib.sha256(value)
        elif mode == "sha512":
            h = hashlib.sha512(value)
        elif mode is None:
            h = [hashlib.md5(value), hashlib.sha1(value), hashlib.sha256(value), hashlib.sha512(value)]
        """
        with open(value, "r") as f:
            for l in f.readlines():
                print(hashlib.md5(l.encode('utf-8')))

#   except:
#       print("Wrong argument")
#        exit(2)


def help_msg(mode):
    assert (mode != "s" or "l"), print("mode is not s or l")

    short_help_string = "hc.py -i <input_file -c <hash_value>"
    long_help_string = "{}\n\n\t-h, --hash: Select a specific hash algorithm. " \
                       "If a hash algorithm is not specified, will the program run all hashes, " \
                       "and compare each to the comare string. " \
                       "\nCurrent algorithms supported: md5, SHA1, SHA256, SHA512"

    if mode == "s":
        print(short_help_string)
        exit(2)
    elif mode == "l":
        print(long_help_string)
        exit(0)


if __name__ == "__main__":
    main()
    # main(sys.argv[1:])
