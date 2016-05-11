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
from colorama import Fore, Back, Style
import random

class Cipher:
    """Cipher Base Class"""
    
    def __init__(self, arguments):
        """Constructor"""
        self.arguments = arguments
        self.plaintext_file = self.arguments['<plaintext>']
        self.ciphertext_file = self.arguments['<ciphertext>']
        
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def GenerateKey(self):
        """Generate Key"""
        self.key = list(deque(self.alphabet).rotate(-3))
    
    def GenerateKeymap(self):
        """Generate Keymap"""
        self.keymap = dict(zip(self.alphabet, self.key))
        
    def Encrypt(self):
        """Encrypt Plaintext"""
        plaintext = list(self.plaintext)
        ciphertext = plaintext

        # Perform replacement
        index = 0
        for letter in plaintext:
            if letter.lower() in self.keymap:
                ciphertext[index] = self.keymap[letter.lower()]

            index += 1

        self.ciphertext = "".join(ciphertext)
    
    def ReadPlaintext(self):
        """Read plaintext file into string"""
        with open(self.plaintext_file, 'r') as ptf:
            self.plaintext = ptf.read()
    
    def WriteCipherText(self):
        """Write ciphertext to the file"""
        with open(self.ciphertext_file, 'w') as ctf:
            ctf.write(self.ciphertext)
    
    def Run(self):
        """Run"""
        self.ReadPlaintext();
        self.Encrypt();
        self.WriteCipherText();
        self.Print();
        
    def PrintPlaintext(self):
        """Print Plaintext"""
        print("PLAINTEXT\n")
        print(Fore.GREEN + self.plaintext + Fore.RESET)
    
    def PrintCiphertext(self):
        """Print Ciphertext"""
        print("CIPHERTEXT\n")
        print(Fore.RED + self.ciphertext + Fore.RESET)
        
    def Print(self):
        """Print Plaintext and Ciphertext"""
        self.PrintPlaintext();
        self.PrintCiphertext();

class MonoalphabeticCipher(Cipher):
    """Implements a monoalphabetic cipher"""

    def __init__(self, arguments):
        """Constructor"""
        super().__init__(arguments);
        self.random = arguments['--random']
        self.shift = arguments['--caesar']

        if self.shift:
            self.shift = int(self.shift)
        else:
            self.shift = 0;

        # Generate a key and keymap
        self.GenerateKey()
        self.GenerateKeymap()

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

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.0')
    # print(arguments)

    # Run the Monoalphabetic Cipher
    cipher = MonoalphabeticCipher(arguments);
    cipher.Run();
