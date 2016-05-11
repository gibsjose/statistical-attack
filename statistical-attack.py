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


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.0')
    print(arguments)
