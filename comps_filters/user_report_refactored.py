
#! /usr/bin/env python3

import os

pwd_file = open("/etc/passwd") #read the file /etc/passwd

pwd_file_line = pwd_file.readlines() #read the file one line at a time

def get_user(pwd_file_line): #gets the user we want from the /etc/passwf file
    
    pwd_file_line = pwd_file_line.rstrip() #removes all empty spaces
    passwd_fields = pwd_file_line.split(':') #splits into lines using the : as reference
    if int(passwd_fields[2]) >= 1000 or int(passwd_fields[2]) == 0: #gets the user with user id of 0 and bigger than 1000
        return True
    else:
        return False


def parse_group(group_path='/etc/group'): #gets the group info from the /etc/group file
    group_data = []
    with open(group_path) as group_file: #read the file /etc/group and assigns its value to group_file
        group_file_strings = group_file.readlines() #reads the file on line at a time and assigns the value to group_file_string
        for group_line in group_file_strings: #loops the groups over the whole list of groups
            group_line = group_line.rstrip()
            group_data.append(group_line.split(':')) #creates a list of the groups
    return group_data

def get_sup_groups(username, group_data): #this will loop the users over the group list
    
    for user in username:
        sup_groups = [] #creates a empty list for each user
        for group in group_data: 
            if user[0] in group[3]: #checks the first position on user over the third on group
                sup_groups.append(group[0]) #appends the user name to the group list
        user.append(sup_groups) #appends sup group info to each user 
    return username

def gen_user_report(users_sup_groups, output_file='user_report.txt'):

    file_dir = os.path.dirname(__file__)
    file_path = os.path.join(file_dir, 'user_report.txt') #uses the current directory
    over_write_file = open(file_path, 'w') #opens the file with write privilege

    for user in users_sup_groups: #will loop over the users, lines, in users_sup_groups

        text = """
        Account Name: {}
        UID: {}
        GID: {}
        Home Dir: {}
        Shell: {}
        Supplimentary Groups: {}
        """.format(user[0], user[2], user[3], user[5], user[6], user[7]) #gets in each line from users_sup_groups, the information to be added on each {}

        over_write_file.write(text) #after each loop, it writes the file, add the information about the user

    over_write_file.close() #it closes the file after all the users be checked

def main(): #this makes all these functions bellow run when the python file is invoked
   
    user_accounts = list(filter(get_user, pwd_file_line))
    group_data = parse_group()
    users_sup_groups = get_sup_groups(user_accounts, group_data)
    gen_user_report(users_sup_groups)

if __name__ == '__main__': #this makes the python file, program, runs by itself, when called, invoked
    main()

