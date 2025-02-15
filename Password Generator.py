print("Welcome to password generator!")
import random
import string

passLength = int(input("length of pass: "))
def simple_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=length))
    print(password)
    file1= open("pass_save.txt", "a")
    file1.write(f"\n{password}")
    file1.close()
    return password

simple_password(passLength)
