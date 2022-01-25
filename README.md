# python-study-repository
This repository includes the process of learning python, including basic knowledge, object-oriented programming (OOP),web crawler, classic cryptography, pygame and machine learning.

## basic grammar

## object-oriented programming (OOP)

## Web crawler
Some interesting and simple examples of web crawler, realize from BIT public class in MOOC. 

## Classic cryptography
Some classic cryptography coding and encoding program, include morse code, virginia cipher(caesar), fence cipher, qwe transfer, and jiujian(9-keys) transfer.

interface1.py
A generalized interface where user can choose encryption/decryption mode.

morse_code.py
Complete the function of converting Morse code into corresponding numbers or letters or digital letters into passwords, suitable for different symbols of dots, dashes and intervals. User can costumize symbol for dash, dot and interval.
To be improved: Some passwords are separated by more than one character, and some passwords have different interval symbols between letters and letters, words and words.
https://en.wikipedia.org/wiki/Morse_code

virginia_cipher.py
Virginia cipher encryption and decryption Achieved: English characters can have spaces, encryption and decryption are reversed To be improved: cannot be used to encrypt non-English characters (numbers and Chinese punctuation marks), all upper and lower case will be converted to lower case.
Advantage: almost impossible to crack without the key.
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
https://en.wikipedia.org/wiki/Caesar_cipher
User can costumize the key of virginia cipher and offset of caeser cipher. Without knowing offset of caeser cipher, it can be decrypted violently.

fence_cipher.py
Fence cipher encryption and decryption Achieved: It can encrypt a piece of English characters, Chinese characters, numbers or other symbols, or a combination of the above methods, and has a wide range of applications (but encrypted Chinese can be easily deciphered) In the case that it is determined to be fence encryption but the fence width is unknown, brute force can be cracked, and the iteration length is between 2 and 1/2 the length of the character to be deciphered. Password disadvantage: easy to be deciphered (especially with spaces or Chinese characters) Encryption and decryption are reciprocal (in the case of spaces, there may be small problems that do not affect reading, such as conjunctions; or big problems: encrypted text, if spaces appear at the end or beginning, when copying Missing a space causes the decryption to be garbled) Multi-encryption, reverse input fence width when decrypting

jiujian_transfer.py qwe_transfer.py
These two files transfer text by 9-keys-keyboard and 26-keys-keyboard(qwe)

## pygame

## machine learning
