from multiprocessing import Pool
import time
import os
import signal
import sys
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
                print(f"Password is: {pwd}")
                print(f"{time.time() - starttime}s")
                # If one of the processes finds the password, call the main program to tell the other processes to stop
                os.kill(os.getppid(), signal.SIGUSR1)
                return True
            except:
                return False
        elif compressedFileFormat == "R":
            try:
                file = rarfile.RarFile(compressed_file)
                file.extractall(path = targetLocation, pwd = pwd)
                print(f"Password is: {pwd}")
                print(f"{time.time() - starttime}s")
                # If one of the processes finds the password, call the main program to tell the other processes to stop
                os.kill(os.getppid(), signal.SIGUSR1)
                return True
            except:
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
        return False

# Brute-forcing archives with various passwords
def brute_forcer(head: list):
    # The password length is arranged from 1 to 10
    # A B C D E F G H I J ...
    # AA AB AC AD ... BA BB BC BD ... CA CB CC CD ...
    # AAA AAB AAC AAD ... BAA BAB BAC BAD ... CAA CAB CAC CAD ...
    for passlen in range(1, 11):
        for i in head:
            # If you find the compressed file password, jump out
            if(pwd_gen(passlen, i) == True):
                return

def handle(signum, frame):
    sys.exit()

# Assign workload to process
def load_balancer(pn: int):
    single_load = int(len(dictionary)/pn)
    arg_list = []
    dic_ind = 0
    # Assign alphanumeric to process
    # Suppose there are only 14 English letters: A B C D E F G H I J K L M N
    # The result:
    # Process 1: A B C D, Process 2: E F G H, Process 3: I J K L
    for i in range(pn):
        arg = []
        for j in range(single_load):
            arg.append(dictionary[dic_ind])
            dic_ind += 1
        arg_list.append(arg)
    
    # Assign the remaining unassigned alphanumerics to the process
    # The result:
    # Process 1: A B C D M, Process 2: E F G H N, Process 3: I J K L
    j = 0
    for i in range(dic_ind, len(dictionary)):
        arg_list[j].append(dictionary[dic_ind])
        j += 1
        dic_ind += 1
    signal.signal(signal.SIGUSR1, handle)
    global starttime
    starttime = time.time()
    # Multiple processes violently decompress compressed files according to the assigned workload
    Pool(pn).map(brute_forcer, arg_list)
    
# Choose the format of the extracted archive
while True: 
    compressedFileFormat = input("Please enter the desired zip file format (Z: Zip, R: RAR): ")
    if compressedFileFormat == 'Z' or compressedFileFormat == 'R':
        break
    
# Determine the number of processes
proc_num = int(input("How many processes? "))
set_dictionary()
load_balancer(proc_num)