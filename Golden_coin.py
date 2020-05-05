#!usr/bin/env python
#-*- coding: utf-8 -*-

############################################
# Golden coin / try your chois @by Xenoret #
############################################

import os, random #import libs

os.system('cls||clear') # Clear terminal

print('=====' *10)
print('\t\tGolden ocin')
print('=====' *10)
eagle = 1
tails = 2
def coin(eagle, tails):
    print('This golden coin, will decide how you do\n')
    rand = random.randint(1, 3) # Random try value
    if rand == 1:
        print('Eagle!\nGo to sleep.')
    elif rand == 2:
        print('Tails!\nGo back to code.')
    else:
        print('Rib coin!\nFree time.')
coin(eagle, tails) #Write inputs
