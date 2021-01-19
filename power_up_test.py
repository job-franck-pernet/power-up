#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

__author__ = "Franck Pernet"
__license__ = ""
__version__ = "2021-01-18"
__email__ = "job.franck.pernet@gmail.com"

import sys
from anki.anki_class import anki 

if __name__ == "__main__":
  deck_file = "./deck_art.txt"
  if 2 == len(sys.argv):
    deck_file = sys.argv[1]
  try:
    my_anki = anki(deck_file)
    my_anki.session()
  except KeyboardInterrupt:
    print("\nSession interrupted, see you soon.")
  
