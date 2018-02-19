#! /usr/bin/env python3
#read the file "etc/passwd"
pwd_file = open("/etc/passwd")
#pwd_file_string = pwd_file.read()
#print(pwd_file_string)
#read the file one line at a time
pwd_file_line = pwd_file.readlines()
#print(pwd_file_line)
def createAList(file_list): #defines a function to replace de : for ,, in the list.
    file_list = file_list.replace(":", ",") #replace ; by ,
    file_list = file_list.lower() #turns all letters into lower
    file_list = file_list.split(" ") #split into a list

    return file_list


