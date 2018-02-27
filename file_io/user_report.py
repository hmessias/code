#! /usr/bin/env python3

pwd_file = open("/etc/passwd") #read the file /etc/passwd

#print(pwd_file_string)
pwd_file_line = pwd_file.readlines() #read the file one line at a time


def get_user_accounts(file_list):
    user_accounts = []
    
    for passwd_line in file_list:
        passwd_line = passwd_line.rstrip()
        passwd_fields = passwd_line.split(':')
        if int(passwd_fields[2]) >= 1000 or int(passwd_fields[2]) == 0:
            user_accounts.append(passwd_fields)
    return user_accounts

def parse_group(group_path='/etc/group'):
    group_data = []
    with open(group_path) as group_file: #read the file /etc/passwd
        group_file_strings = group_file.readlines()
        for group_line in group_file_strings:
            group_line = group_line.rstrip()
            group_data.append(group_line.split(':'))
    return group_data

def get_sup_groups(username, group_data):
    sup_groups = []
    for group in group_data:
        if username in group[3]:
            sup_groups.append(group[0])
    return sup_groups


group_data = parse_group()
user_accounts = get_user_accounts(pwd_file_line)
htpadmin_sup_groups = get_sup_groups("htpadmin", group_data)

