import random
import string
password=[]
for i in range(0,10):
    password.append(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation))
random.shuffle(password)
shuffuled_password=" "
for i in password:
    shuffuled_password+=i
print(shuffuled_password)