#!/usr/bin/env python

__author__ = "Supreme Ciento"
__copyright__ = "Copyright (C) 2020 CloudBots™"
__license__ = "GNU 3.0"
__version__ = "0.1.1"
__email__ = "cloudbotsbiz@gmail.com"
__status__ = "Dev"

import time
from time import sleep

logo = """
+dddddddddddddddddddddddddddddy++++++++++++++++++:
sMMMMMMMMMMMMMMMMMNdhysoooosyhmNMMMMMMMMMMMMMMMMMs
sMMMMMMMMMMMMMds/.              ./sdMMMMMMMMMMMMMs
sMMMMMMMMMMd+`                      `+dMMMMMMMMMMs
sMMMMMMMMy-      .:+ooo+/:`            -yMMMMMMMMs
sMMMMMMd-     :yNMMMMMMMMM-              -dMMMMMMs
sMMMMMo     -mMMMms/:--/os                 oMMMMMs
sMMMM/     -NMMM+                           /MMMMs
sMMM+      dMMM+                             oMMMs
sMMd      `MMMM.                              dMMs
sMM/       NMMM+                              /MMs
sMM`       /MMMMh/-..-/o   `::::::--`         `MMs
sMN         -hMMMMMMMMMo   sMMMMMMMMMm+        NMs
sMM`          `:+ssso+:`  `NMMN---oMMMM.      `MMs
oMM/                      +MMMo   .MMMm`      /MMo
.MMd                      mMMMdhhmMmh+`       dMM.
.MMMo                    :MMMmhhdNMMd+       oMMM.
.MMMM/                   hMMM:   `NMMM:     /MMMM.
.MMMMMo                 .MMMm   `+MMMM.    oMMMMM.
.MMMMMMd-               sMMMMNNMMMMMh-   -dMMMMMM.
.MMMMMMMMy-             +ooooooo+/-`   -yMMMMMMMM.
.MMMMMMMMMMd+`                      `+dMMMMMMMMMM.
.MMMMMMMMMMMMMds/.              ./sdMMMMMMMMMMMMM.
.MMMMMMMMMMMMMMMMMNmhysoooosyhmNMMMMMMMMMMMMMMMMM.
.dddddddddddddddddddddddddddddy++++++++++++++++++`
"""
print(logo)
sleep(3)

print('\n')

print("--Sieve Of Eratosthenes, 'SoE' 2020, CloudBots™--: ")
print('--Email: CloudBotsBiz@Gmail.com--: ')
print('--Press CTRL+C to End Session--: ')
print('\n')
print('-PREREQUISITES-')
print("1): Enter a number to find the primes preceeding it:")
print('\n')
sleep(2)

def Primes(upperLimit):
    primes = list(range(2,upperLimit+1))
    for i in primes:
            j = 2
            while i * j <= primes[-1]:
                    if i * j in primes:
                        primes.remove(i*j)
                    j += 1
    print('\n')
    print('Here are the prime numbers preceeding your entry:')
    print('\n')
    print(primes)

while True:
    Entry = input('Enter a number: ')  
    x = int(Entry)  
    Primes(x)