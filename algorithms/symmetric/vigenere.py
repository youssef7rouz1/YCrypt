"""
Vigenere
Functions:
- encrypt(plaintext: str, key: str , alphabet : str) -> str
- decrypt(ciphertext: str, key: str , alphabet : str) -> str

input text must have only letters
user can change the alphabet 
"""
import string # used for string manipulation
from typing import List , Tuple

def generate_vigenere_table(alphabet : str) -> list[list[str]]:
    """
    Generates the vigenere table given a set of letters (alphabet)
    
    """
    n = len(alphabet)
    table: list[list[str]] = []
    alphabet=alphabet.upper() # vigenere table is all uppercase
    for i in range(n):
        # shift the alphabet left by i positions
        shifted = alphabet[i:] + alphabet[:i]
        table.append(list(shifted))
    return table


def generate_full_key(key  : str ,length : int ) -> str :
    """
    Generates the full key given the keyword
    
    """
    result=[]
    input=key.replace(" " , "")     #ignore all spaces in the keyword
    
    for i in range(length):         #length here will be used to correspond to the length of the plaintext 
                                    #since plain and key must ahve same length
        index=i % len(input)        #repeat the key if the lengt of the plaintext is bigger then the length of the keyword
        result.append(input[index])
    return ''.join(result).upper() #return the key as a string

def store_space_positions(text : str) -> list:
    """
    Stores the spaces positions in a given string .
    Used in vigenere cipher since we clean the texts by removing the spaces .
    
    """
    result=[]
    for i in range(len(text)):
        if text[i]==" ":
            result.append(i)
    return result

            



def encrypt(plaintext: str, key: str , alphabet : str) -> str:
    """
    Encrypts plaintext using Vigenere cipher.
    
    """
    result=[] # vaariable ti store the result of encryption
    space_positions=store_space_positions(plaintext) #stores the spaces' positions to add them later in the cipher
    input = plaintext.replace(" ", "") #remove the spaces in the text
    final_key=generate_full_key(key , len(input))
    vigenere_table=generate_vigenere_table(alphabet)


    for i  in range(len(input)): # for each letter in the plaintext
        ch = input[i]
        
           
        if ch.isupper(): #if plain letter is upper , the cipher letter will be upper
            
            result.append((vigenere_table[ord(ch)-65][ord(final_key[i])-65]).upper())
        else : #if plain letter is lower , the cipher letter will be lower
            result.append((vigenere_table[ord(ch)-97][ord(final_key[i])-65]).lower())
                

  
    for i in space_positions:
        result.insert(i , " ") # insert the spaces in the ciphertext
    return ''.join(result) # return the result as a string


def decrypt(ciphertext: str, key: str , alphabet : str ) -> str:
    """
    Decrypts ciphertext using Vigenere cipher.
    
    """
    result=[]
    space_positions=store_space_positions(ciphertext)
    input = ciphertext.replace(" ", "")
    final_key=generate_full_key(key , len(input))
    vigenere_table=generate_vigenere_table(alphabet)

  
    for i  in range(len(final_key)): # for each letter in the key
        cipher_letter=input[i]
        key_letter = final_key[i]
        column=[row[ord(key_letter)-65] for row in vigenere_table] # extract the corresponding column
        index=column.index(cipher_letter.upper()) # find the index of the row containing the plaintext letter
        
       
        
        plain_letter=vigenere_table[0][index]
           
        if cipher_letter.isupper():
            
            result.append(plain_letter.upper())
        else : 
            result.append(plain_letter.lower())
                

  
    for i in space_positions:
        result.insert(i , " ")
    return ''.join(result)



