#!/usr/bin/env python3
"""Pseudo-secure Monoalphabetic Cipher Encryption

Usage:
  encrypt.py <input> <output> [--random | --caesar=<shift>]
  encrypt.py (-h | --help)
  encrypt.py --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  --random          Randomly generate the substitution letters
  --caesar=<shift>  Use simple Caesar Cipher with given shift

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.0')
    print(arguments)
