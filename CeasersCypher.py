import string
import itertools

def Ceasers(text,shiftby,cipher_direction):
    alphabet_set=list(string.ascii_lowercase+string.ascii_lowercase)
    end_text=""
    if cipher_direction=="decode":
            shiftby=shiftby*-1
    for i in text:
        position=alphabet_set.index(i)
        new_position=position+shiftby
        end_text+=alphabet_set[new_position]
    print(f"the {cipher_direction}d text is {end_text}")

direction=input("enter 'encode' for encryption and 'decode' for decrypt\n").lower()
code=(input("enter your message: \n")).lower()
shift=int(input("type the shift number: \n"))

Ceasers(code,shift,direction)

