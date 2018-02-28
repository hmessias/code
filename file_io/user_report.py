#! /usr/bin/env python3

import os

pwd_file = open("/etc/passwd") #read the file /etc/passwd

pwd_file_line = pwd_file.readlines() #read the file one line at a time


def get_user_accounts(file_list): #gets the user we want from the /etc/passwf file
    user_accounts = [] #creates an empty user_accounts list to be filled with the info we want
    
    for passwd_line in file_list:
        passwd_line = passwd_line.rstrip() #removes all empty spaces
        passwd_fields = passwd_line.split(':') #splits into lines using the : as reference
        if int(passwd_fields[2]) >= 1000 or int(passwd_fields[2]) == 0: #gets the user with user id of 0 and bigger than 1000
            user_accounts.append(passwd_fields) #appends this information to the user_accounts list
    return user_accounts

def parse_group(group_path='/etc/group'): #gets the group info from the /etc/group file
    group_data = []
    with open(group_path) as group_file: #read the file /etc/group
        group_file_strings = group_file.readlines() #reads the file on line at a time and assigns the value to group_file_string
        for group_line in group_file_strings: #loops the 
            group_line = group_line.rstrip()
            group_data.append(group_line.split(':'))
    return group_data

def get_sup_groups(username, group_data): #this will loop the users over the group list
    
    for user in username:
        sup_groups = [] #creates a empty list for each user
        for group in group_data: 
            if user[0] in group[3]: #checks the first position on user over the third on group
                sup_groups.append(group[0]) #appends the user name to the group list
        user.append(sup_groups) #appends sup group info to each user 
    return username



group_data = parse_group()
user_accounts = get_user_accounts(pwd_file_line)
users_sup_groups = get_sup_groups(user_accounts, group_data)
print(users_sup_groups)
