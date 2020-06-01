#!usr/bin/env python
#-*- coding: utf-8 -*-

############################################
# Golden coin / try your chois @by Xenoret #
############################################

import os #import lib
import random #import lib

os.system('cls||clear') # Clear terminal

print('=====' *10)
print('\t\tGolden coin')
print('=====' *10)

def coin():
    print('This golden coin, will decide how you do\n')
    rand = random.randint(1, 3) # Random try value
    
    if rand == 1:
        print('Eagle!\nGo to sleep.')
    
    elif rand == 2:
        print('Tails!\nGo back to code.')
    
    else:
        print('Rib coin!\nFree time.')
coin() #Call def
