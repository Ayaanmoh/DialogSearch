#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:10:34 2020

@author: ayaan
"""

import re

res=[]

with open('dracula.txt', 'r') as infl:
    hand = infl.read()

match = re.findall('(?:"(.*?)")', hand)

for item in match:
    res.append('"' + item + '"' )




word="CHAPTER"
sent="this is a sentence this this"
indices=[]

for match in re.finditer(word, hand):
    indices.append(match.start())


parts = [hand[i:j] for i,j in zip(indices, indices[1:]+[None])]
print(parts[5])


if "Journal" in parts[5]:
    print("hello")
