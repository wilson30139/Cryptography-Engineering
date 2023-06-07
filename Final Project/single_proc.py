import time
import zipfile
from unrar import rarfile

compressed_file = "C:\\Users\\[userName]\\Desktop\\test.zip"
# Where to place the archive after decompression
targetLocation = "C:\\Users\\[userName]\\Desktop\\"
compressedFileFormat = "Z"
dictionary = []

# Build an alphanumeric dictionary
def set_dictionary():
    for i in range(ord('A'), ord('Z')+1):
        dictionary.append(chr(i))
    for i in range(ord('a'), ord('z')+1):
        dictionary.append(chr(i))
    for i in range(ord('0'), ord('9')+1):
        dictionary.append(chr(i))

# Automatically generate passwords by looking up an alphanumeric dictionary
def pwd_gen(length: int, pwd: str) -> bool:
    # Whether the length of the currently combined password is equal to the length of the password to be arranged
    if (len(pwd) == length):
        if compressedFileFormat == "Z":
            try:
                file = zipfile.ZipFile(compressed_file, 'r')
                file.extractall(path = targetLocation, pwd = pwd.encode('utf-8'))
                print(f"\nCracked and extracted! Password: {pwd}")
                print(f"{time.time() - starttime}s")
                return True
            except:
                print(f"Incorrect password tried: {pwd}")
                return False
        elif compressedFileFormat == "R":
            try:
                file = rarfile.RarFile(compressed_file)
                file.extractall(path = targetLocation, pwd = pwd)
                print(f"\nCracked and extracted! Password: {pwd}")
                print(f"{time.time() - starttime}s")
                return True
            except:
                print(f"Incorrect password tried: {pwd}")
                return False
    # If not, continue to combine the current password (increase password length)
    # If the length of the current combined password is already equal to the length of the password to be arranged,
    # start to arrange at a certain length
    else:
        for i in dictionary:
            temp = pwd
            temp += i
            if(pwd_gen(length, temp) == True): 
                return True
    
# Brute-forcing archives with various passwords
def brute_forcer():
    global starttime
    starttime = time.time()
    # The password length is arranged from 1 to 10
    # A B C D E F G H I J ...
    # AA AB AC AD ... BA BB BC BD ... CA CB CC CD ...
    # AAA AAB AAC AAD ... BAA BAB BAC BAD ... CAA CAB CAC CAD ...
    for passlen in range(1, 11):
        # If you find the compressed file password, jump out
        if(pwd_gen(passlen, "") == True):
            break

# Choose the format of the extracted archive
while True: 
    compressedFileFormat = input("Please enter the desired zip file format (Z: Zip, R: RAR): ")
    if compressedFileFormat == 'Z' or compressedFileFormat == 'R':
        break

set_dictionary()
brute_forcer()