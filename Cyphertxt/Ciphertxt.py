########################################################################
##
## CS 101
## Program #4
## Diego Brown
## xxxxxx@xxxx.xxxx.edu
##
## PROBLEM : To be able to Encipher File and Decipher File   
##
## ALGORITHM :
##Get input from user for Transposition Options
##1.	Encipher File
##2.	Dicipher File
##3.	Quit
##If input = 1 or input 2 
##	Request the name of file to write to
##	If file name is not there
##	Warn user it is not found and try another file name.
##If = 1
##	Prompt user for the file name to Encipher
##		If it’s not valid
##		Prompt user to try another filename
##  Enter the name of the file to write to decode to 
##	Output the file has been transposed.
##      Print the original line from file
##      Get the beginning of the string and end of the string( Move all the odd index characters to the end of the sting.
##      Print the Transpose line from file
##If = 2
##	Prompt user for the file name to Decode
##		If it’s not valid
##		Prompt user to try another filename
##Enter the name of the file to write to decode to 
##	Output the file has been untransposed.
##      Print the orginal line from file
##      Get the beginning of the string and end of the string( Move all the odd index characters to the end of the sting.
##      Print the un-transpose line from file
##      
## 
## ERROR HANDLING:
##      Menu options
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#Import

import os.path
import math

#Defining global vaules
continue_deciphering = True
correct_input = False
file_to_transpose = ""
file_to_write = ""
to_do_message = ""
file_found = False
file_created = False

#Splitting lines

def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

#Opening a file

def open_txt_file(file_name):
    does_exist = os.path.isfile(file_name)
    if does_exist:
        return does_exist
    else:
        print("Could not find the file specified. Try another file name.")

        return does_exist
#Creating a file
    
def create_file(file_name):
    try:
        open(file_name, "w+")
        return True
    except:
        print("The file specified had an IO Error")
        return False
    
#Transposing a file
    
def transpose(original):
    new_message = ""
    for line in original:
        c_line = split_len(line, 1)
        new_line = ""
        even_char = ""
        odd_char = ""
        count = 0
        for char in c_line:
            if count % 2 == 0:
                even_char = even_char + char
            else:
                odd_char = odd_char + char
            count += 1

        new_line = even_char.replace("\n", "") + odd_char.replace("\n", "")
        new_message = new_message + new_line + "\n"
    original.close()
    return new_message
#Untranspose a file
def untranspose(message):
    new_message = ""
    for line in message:
        new_line = ""
        even_char = line[:math.ceil(len(line.replace("\n", "")) / 2)]
        odd_char = line[math.ceil(len(line.replace("\n", "")) / 2):]
        count = 0
        e_count = 0
        o_count = 0
        while count < len(line.replace("\n", "")):
            if count % 2 == 0:
                new_line = new_line + even_char[e_count]
                e_count += 1
            else:
                new_line = new_line + odd_char[o_count]
                o_count += 1
            count += 1
        new_message = new_message + new_line + "\n"
    return new_message

#Writing to a file

def write_to_file(message, file_to_change):
    file_to_change.write(message)
    file_to_change.close()

#Defining values

while continue_deciphering:

    correct_input = False
    file_to_transpose = ""
    file_to_write = ""
    to_do_message = ""
    file_found = False
    file_created = False

#Displaying menu options
    
    while not correct_input:
        print("Transposition Options")
        print("")
        print("1. Encipher File")
        print("2. Decipher File")
        print("Q. Quit")
        to_do_message = input("==> ")
        if to_do_message == "1" or to_do_message == "2" or to_do_message == "q" or to_do_message == "Q":
            correct_input = True
        else:
            print("You must enter 1, 2, Q")

    if to_do_message == "q" or to_do_message == "Q":
        break
#Correcting errors
    
    while not file_found:
        if to_do_message == "1":
            file_to_transpose = input("Enter the name of the file to encipher ==> ")
        elif to_do_message == "2":
            file_to_transpose = input("Enter the name of the file to decode ==> ")
        file_found = open_txt_file(file_to_transpose)

    file_to_transpose = open(file_to_transpose)

    while not file_created:
        file_to_write = input("Enter the name of the file to write to ==> ")
        file_created = create_file(file_to_write)

    file_to_write = open(file_to_write, "w+")

    if to_do_message == "1":
        write_to_file(transpose(file_to_transpose), file_to_write)
    elif to_do_message == "2":
        write_to_file(untranspose(file_to_transpose), file_to_write)
