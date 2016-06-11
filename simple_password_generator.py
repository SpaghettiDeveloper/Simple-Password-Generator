#!/path/to/python3
# -*- coding: utf-8 -*-

'''
COPYRIGHT (c) 2016 <Stefano Peris>

MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
'''
--------------------------------------
Created on 11 giu 2016

@author: SpaghettiDeveloper
@email: stefano.peris.dev@gmail.com
--------------------------------------
'''

import string
from random  import *
import os

os.system('cls')
characters = string.ascii_letters+string.punctuation+string.digits
password = "".join(choice(characters) for x in range(randint(9, 16)))

print("--- SIMPLE-PASSWORD-GENERATOR ---")
print("")
print ("--- author: SpaghettiDeveloper")
print ("--- email: stefano.peris.dev@gmail.com")
print("")
print("Password Generated: ", password)
