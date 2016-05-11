#!/usr/bin/env python3
"""Monoalphabetic English Statistical Attack

Usage:
  statistical-attack.py <ciphertext> [--depth=<depth>]
  statistical-attack.py (-h | --help)
  statistical-attack.py --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  --depth=<depth>   Depth of statistical attack (monograms, bigrams, etc.) [default: 1]

"""
from docopt import docopt
from collections import deque
from colorama import Fore, Back, Style
import random

class Statistics:
    """Statistics"""
    
    def __init__(self, ciphertext):
        """Constructor"""
        self.ciphertext = ciphertext
     

class StatisticalAttack:
    """Statistical Attack"""
    
    def __init__(self, arguments):
        """Constructor"""        
        self.ciphertext_file = arguments['<ciphertext>']
        self.depth = arguments['--depth']
        
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def ReadCiphertext(self):
        """Read ciphertext file into string"""
        with open(self.ciphertext_file, 'r') as ctf:
            self.ciphertext = ctf.read()
            
    def Analyze(self):
        """Analyze ciphertext"""
        self.statistics = Statistics(self.ciphertext)
    
    def GenerateKey(self):
        """Determine the key from the ciphertext analysis"""
        self.key = list(self.alphabet)
    
    def GenerateKeymap(self):
        """Generate Keymap"""
        self.keymap = dict(zip(self.key, self.alphabet))
        
    def Decrypt(self):
        """Decrypt Ciphertext"""
        ciphertext = list(self.ciphertext)
        plaintext = ciphertext

        # Perform replacement
        index = 0
        for letter in ciphertext:
            if letter.lower() in self.keymap:
                plaintext[index] = self.keymap[letter.lower()]

            index += 1

        self.plaintext = "".join(plaintext)
    
    def Run(self):
        """Run"""
        self.ReadCiphertext()
        self.Analyze()
        self.GenerateKey()
        self.GenerateKeymap()
        self.Decrypt()
        self.Print()
    
    def PrintCiphertext(self):
        """Print Ciphertext"""
        print("CIPHERTEXT\n")
        print(Fore.RED + self.ciphertext + Fore.RESET)
        
    def PrintPlaintext(self):
        """Print Plaintext"""
        print("PLAINTEXT\n")
        print(Fore.GREEN + self.plaintext + Fore.RESET)
        
    def Print(self):
        """Print Ciphertext and Plaintext"""
        self.PrintCiphertext();
        self.PrintPlaintext();
        
if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.0')
    # print(arguments)
    
    attack = StatisticalAttack(arguments)
    attack.Run()
