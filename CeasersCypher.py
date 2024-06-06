import string
user_input=input("enter 'encode' for encryption and 'decode' for decrypt\n")
def encryption():
    code=input("enter your message: \n")
    shift=int(input("type the shift number: \n"))
    first_set=list(string.ascii_lowercase)
    shifted_set=list(string.ascii_lowercase)
    i=0
    while i<(26-shift):
        shifted_set[i]=first_set[shift+i]
        i=+1
    print(shifted_set)
if user_input=="encode":
    encryption()
# if user_input=="decode":
#     decryption()
string.