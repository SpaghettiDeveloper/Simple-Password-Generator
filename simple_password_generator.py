#!/path/to/python3
# -*- coding: utf-8 -*-

'''
Created on 11 giu 2016

@author: StepDevelop
'''

import string
from random  import *
characters = string.ascii_letters+string.punctuation+string.digits
password = "".join(choice(characters) for x in range(randint(9, 16)))
print("Password Generated:")
print(password)