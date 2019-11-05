import string, re, os
import numpy as np

"""No guarantee that any of this is even remotely correct...

Used for ciphers, often used simple ones.
"""

def caesar(text, shift):
    lc = string.ascii_lowercase
    new = ''
    for t in text:
        if t in lc:
            new += lc[(lc.index(t) + len(lc) + shift) % len(lc)] # "+len(lc)" to accomodat negative shifts
        else: new += t
    return new
    
    
def alt_caesar(text, seq):
    """Do Caesar, but have the shifts loop through seq, instead of using a single constant shift"""
    lc = string.ascii_lowercase
    new = ''
    
    lseq = len(seq)
    ltext = len(text)
    numberrot = round(ltext/lseq) + 1
    
    for t, shift in zip(text, seq*numberrot):
#         print(t, shift)
        if t in lc:
            new += lc[(lc.index(t) + len(lc) + shift) % len(lc)] # "+len(lc)" to accomodat negative shifts
        else: new += t
    return new
    
def vigenere_encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [lc.index(i) for i in key]
    print(key_as_int)
    plaintext_int = [lc.index(i) for i in plaintext]
    ciphertext = ''
    for i, char in enumerate(plaintext_int):
        value = (char + key_as_int[i % key_length]) % 26
        ciphertext += lc[value]
   
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [lc.index(i) for i in key]
    ciphertext_int = [lc.index(i) for i in ciphertext]
    plaintext = ''
    for i, char in enumerate(ciphertext_int):
        value = (char - key_as_int[i % key_length]) % 26
        plaintext += lc[value]
    return plaintext



def bifid_encrypt(key, plaintext):
    """Key is used to construct the cypher rectangle, 
    then the plaintext is converted to coordinates, 
    and the coordinates to cyphertext."""
    
    # preprocessing fo strings
    key = key.upper()
    plaintext = plaintext.upper()
    
    key = key.replace('J', 'I')
    key = key.replace(" ", "")
    plaintext = plaintext.replace('J', 'I')
    plaintext = plaintext.replace(" ", "")
    
    ascii_upper = string.ascii_uppercase
    ascii_upper = ascii_upper.replace('J', 'I')
    
    
    #Create the bifid cipher rectangle based on the key
    rectangle = ''
    for char in key+ascii_upper:
        if char not in rectangle: rectangle += char
    
    if len(rectangle) != 25: 
        print("Something went wrong here", len(rectangle))
        print(rectangle)
        
    print('Using key', key)
    
    # Get the coordinates of the plaintext in the rectangle
    rows = []
    columns = []
    for char in plaintext:
        if not char in ascii_upper:
            c = 'space' if char == " " else char
            print("Omitting", c)
            continue
        position = rectangle.index(char)
        rows.append(int(np.floor(position/5)))
        columns.append(position % 5)
        
    # Convert coordinates back to other characters
    allcoords = rows+columns
    cyphertext = ''
    for i in range(len(rows)):
        these_coords = allcoords[2*i:2*i+2]
        cyphertext += rectangle[5*these_coords[0]+these_coords[1]]
    
    return cyphertext

