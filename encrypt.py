#!/usr/bin/env python3
"""Pseudo-secure Monoalphabetic Cipher Encryption

Usage:
  encrypt.py <plaintext> <ciphertext> [--random | --caesar=<shift>]
  encrypt.py (-h | --help)
  encrypt.py --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  --random          Randomly generate the substitution letters  [default: true]
  --caesar=<shift>  Use simple Caesar Cipher with given shift

"""
from docopt import docopt
from collections import deque
import random

class MonoAlphaCipher:
    """Implements a monoalphabetic cipher"""

    def __init__(self, arguments):
        """Constructor"""
        self.random = arguments['--random']
        self.shift = arguments['--caesar']

        if self.shift:
            self.shift = int(self.shift)
        else:
            self.shift = 0;

        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # Generate a key
        self.GenerateKey()

    def GenerateKey(self):
        """Generate a random/shifted key"""
        # Generate key (substitution letters)
        key = list(self.alphabet)

        if self.random:
            # Generate random key
            random.shuffle(key)
        elif self.shift:
            d = deque(key)
            d.rotate(-1 * self.shift)
            key = list(d)
        else:
            # Default to shift of 3 (i.e., Caesar Cipher)
            self.shift = 3
            d = deque(key)
            d.rotate(-1 * self.shift)
            key = list(d)

        self.key = list(key)

        # Generate lookup table (keymap)
        self.keymap = dict(zip(self.alphabet, self.key))

    def Encrypt(self, plaintext):
        """Encrypt"""
        self.plaintext = list(plaintext)
        self.ciphertext = self.plaintext

        # print("Key:")
        # print(self.key)
        #
        # print("Keymap:")
        # print(self.keymap)

        # Perform replacement
        index = 0
        for letter in self.plaintext:
            if letter.lower() in self.keymap:
                self.ciphertext[index] = self.keymap[letter.lower()]

            index += 1

        return "".join(self.ciphertext)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.0')
    # print(arguments)

    # Get the plain/ciphertext file names
    plaintext_file = arguments['<plaintext>']
    ciphertext_file = arguments['<ciphertext>']

    # Read plaintext file into string
    with open(plaintext_file, 'r') as ptf:
        plaintext = ptf.read()

    # Instantiate a cipher (generates key)
    cipher = MonoAlphaCipher(arguments)

    # Encrypt the plaintext
    ciphertext = cipher.Encrypt(plaintext)

    print("Plaintext: " + plaintext)
    print("Ciphertext: " + ciphertext)

    # Write the ciphertext to the file
    with open(ciphertext_file, 'w') as ctf:
        ctf.write(ciphertext)
