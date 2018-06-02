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

TOTAL_CHARACTERS = 4374127904

MONOGRAM_FILE = 'english-monograms.txt'
BIGRAM_FILE = 'english-bigrams.txt'
TRIGRAM_FILE = 'english-trigrams.txt'
QUADGRAM_FILE = 'english-quadgrams.txt'

class Statistics:
    """Statistics"""
    
    def __init__(self, ciphertext, alphabet):
        """Constructor"""
        self.ciphertext = ciphertext
        self.alphabet = alphabet
        self.frequency_distribution = {}
        self.letter_count = {}
        
        self.DetermineLetterCount()
        self.DetermineFrequencyDistribution()
    
    def DetermineFrequencyDistribution(self):
        """Determine the frequency distribution of the ciphertext"""
        for letter in self.letter_count:
            self.frequency_distribution[letter] = (self.letter_count[letter] / self.total) * 100
        
        # Fill in gaps
        for letter in self.alphabet:
            if letter not in self.frequency_distribution.keys():
                self.frequency_distribution[letter] = 0
        
        print(self.frequency_distribution)
                
    def DetermineLetterCount(self):
        """Determine the count of each letter and the total count"""
        self.total = 0
        
        for letter in self.ciphertext:
            if letter in self.alphabet:
                if letter in self.letter_count.keys():
                    self.letter_count[letter] += 1
                else:
                    self.letter_count[letter] = 1
                
                self.total += 1
                
    def GetFrequencyDistribution(self):
        """Get frequency distribution"""
        return self.frequency_distribution

class StatisticalAttack:
    """Statistical Attack"""
    
    def __init__(self, arguments):
        """Constructor"""        
        self.ciphertext_file = arguments['<ciphertext>']
        self.depth = int(arguments['--depth'])
        
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
        self.ReadNGram()
        
    def ReadNGram(self):
        """Read the correct N-gram file"""
        self.frequency_distribution = {}
                
        # Monogram
        if self.depth == 1:
            with open(MONOGRAM_FILE, 'r') as mf:
                for line in mf.readlines():
                    tokens = line.split()
                    key = str(tokens[0]).lower()
                    frequency = (int(tokens[1]) / TOTAL_CHARACTERS) * 100
                    self.frequency_distribution[key] = frequency
                            
    def ReadCiphertext(self):
        """Read ciphertext file into string"""
        with open(self.ciphertext_file, 'r') as ctf:
            self.ciphertext = ctf.read()
            
    def Analyze(self):
        """Analyze ciphertext"""
        self.statistics = Statistics(self.ciphertext, self.alphabet)
    
    def GenerateKey(self):
        """Determine the key from the ciphertext analysis"""
        # Ciphertext frequency distribution
        cfd = self.statistics.frequency_distribution
        
        # Average frequency distribution
        afd = self.frequency_distribution
        
        
    
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
        self.PrintCiphertext()
        self.PrintPlaintext()
        
if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.0')
    # print(arguments)
    
    attack = StatisticalAttack(arguments)
    attack.Run()
