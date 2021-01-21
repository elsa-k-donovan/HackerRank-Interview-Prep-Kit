#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    dict_words = {}
    
    for m_word in magazine:
        if dict_words.get(m_word) is None:
            dict_words[m_word] = 1
        else:
            dict_words[m_word] += 1
         
    valid = False
    
    for n_word in note:
        
        if dict_words.get(n_word) == 0:
            valid = False
            break
        elif dict_words.get(n_word) is None:
            valid = False
            break
        else:
            dict_words[n_word] -= 1
            valid = True
            continue
    
    if valid:
        print("Yes")
    else:
        print("No")
        
    
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
   
