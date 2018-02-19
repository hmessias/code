#! /usr/bin/env python3

pwd_file = open("/etc/passwd") #read the file /etc/passwd

#print(pwd_file_string)
pwd_file_line = pwd_file.readlines() #read the file one line at a time
print(pwd_file_line)

def changePunctuation(file_list):
    punctuation = ":"
    for i in punctuation:
        file_list = file_list.replace(i, ",")

    return file_list


pwd_file_line = changePunctuation(pwd_file_line)
print(pwd_file_line)