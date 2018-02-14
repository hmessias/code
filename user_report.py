#! /usr/bin/env python3
#read the file "etc/passwd"
pwd_file = open("/etc/passwd")
#pwd_file_string = pwd_file.read()
#print(pwd_file_string)
#read the file one line at a time
pwd_file_line = pwd_file.readlines()
print(pwd_file_line)
for line in pwd_file_line:
    user=[]
    user = 