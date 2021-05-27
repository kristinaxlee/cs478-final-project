# Name: Braden Lee, Kristina Lee, Dwight Kappl
# OSU Spring 2021
# Class: CS478 (Network security)

import math
import sys
import re
from string import punctuation


global length_flag
global special_flag
global lowercase_flag
global uppercase_flag
global number_flag
global space_flag
global common_flag
global personal_flag
global reuse_flag

global special_length
global lower_length
global upper_length
global number_length

def length_of_password(password):
    pass_length = len(password)
    print("password length is:", pass_length)
    print("\n")

    global length_flag

    if (pass_length) < 8:

        # turns flag to false indicating that it's shorter than the recommended length of at least 8 characters
        length_flag = False;

    else:

        #turns flag to true indicating that the password is of sufficient length
        length_flag = True;

    return

def check_for_special_characters(password):

    global special_flag
    global special_length

    special_length = len(re.findall(r'[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', password))

    print("Amount of special characters:", special_length, "\n")

    if(special_length) == 0:

        #turns flag to false indicating that there's no use of special characters within the password
        special_flag = False;

    else:

        #turns flag to true indicating that the password does include usage of at least one special character
        special_flag = True;

    return

def check_for_lowercase(password):

    global lowercase_flag
    global lower_length

    lowers = len(re.findall(r'[a-z]', password))

    lower_length = lowers

    print("Amount of lowercase letters:", lowers, "\n")

    if(lowers) == 0:

        #turns flag to false indicating that there's no use of lowercase characters within the password
        lowercase_flag = False;

    else:

        #turns flag to true indicating that the password does include usage of at least one lowercase character
        lowercase_flag = True;
    

    return
    

def check_for_uppercase(password):

    global uppercase_flag
    global upper_length

    uppers = len(re.findall(r'[A-Z]', password))

    upper_length = uppers

    print("Amount of uppercase letters:", uppers, "\n")

    if(uppers) == 0:

        #turns flag to false indicating that there's no use of uppercase characters within the password
        uppercase_flag = False;

    else:

        #turns flag to true indicating that the password does include usage of at least one uppercase character
        uppercase_flag = True;

    return

def check_for_numbers(password):

    global number_flag
    global number_length

    nums = len(re.findall(r'[0-9]', password))

    number_length = nums

    print("Amount of numbers:", nums, "\n")

    if(nums) == 0:

        #turns flag to false indicating that there's no use of numbers within the password
        number_flag = False;

    else:

        #turns flag to true indicating that the password does include usage of at least one number
        number_flag = True;

def check_for_spaces(password):

    global space_flag

    spaces = len(re.findall(r'[ ]', password))

    print("Amount of spaces:", spaces, "\n")

    if(spaces) >= 1:
        
        #turns flag to false indicating that there's usage spaces within the password (invalid)
        space_flag = False;

    else:
        
        #turns flag to true indicating that the password does not include usage of any spaces (valid)
        space_flag = True;

    return

def check_common_pwd_list(password):
    global common_flag

    common_flag = False

    with open("10-million-password-list-top-1000000.txt") as f:
        Lines = f.read().splitlines() 

    for line in Lines:
        
        if(line == password):

            # if we find the password in the list of common passwords, set flag to True
            common_flag = True
            return

def check_usage(password):

    global personal_flag
    global reuse_flag

    # initialize flags to False
    personal_flag = False
    reuse_flag = False

    personal_info = input("Does your password contain personal information, such as birthdays, children/pet names, maiden names, or your school's name? (y/n)\n")
    
    reuse_password = input("Do you use this same password across multiple platforms? (y/n)\n")

    if(personal_info.lower() == 'y'):
        personal_flag = True   
    
    if(reuse_password.lower() == 'y'):
        reuse_flag = True

    print("\n")

def check_all_flags():

    if(length_flag) == False:
        print("The password:", password, "is short, thus it's relatively weak\n")

    if(special_flag) == False:
        print("The password:", password, "has no usage of any special characters, thus it's weaker than one with special characters\n")

    if(lowercase_flag) == False:
        print("The password:", password, "has no usage of any lowercase characters, thus it's weaker than one with lowercase characters\n")

    if(uppercase_flag) == False:
        print("The password:", password, "has no usage of any uppercase characters, thus it's weaker than one with uppercase characters\n")

    if(number_flag) == False:
        print("The password:", password, "has no usage of any numbers, thus it's weaker than one with numbers\n")

    if(space_flag) == False:
        print("The password:", password, "includes spaces, thus it's a invalid password\n")
    
    if(common_flag) == True:
        print("The password:", password, "was found in the list of common passwords. Please change your password to a more secure password.\n")
    
    if(personal_flag) == True:
        print("The password:", password, "contains personal information which may be easily found on the internet. Hackers may be able to guess your password after finding this information. \nPlease do not include easily found information in your password.\n")
    
    if(reuse_flag) == True:
        print("The password:", password, "is reused across multiple sites, meaning that if one account is breached, many more can be easily breached. Please do not use the same password across multiple websites.\n ")

        
    if((length_flag == 1) and (special_flag == 1) and (lowercase_flag == 1) and (uppercase_flag == 1) and (number_flag == 1) and (space_flag == 1) and (common_flag == False)):
        print("The password:", password, "is relatively strong and secure\n")
              
def check_strength(password):

    #if(special_length) >= 1:

        #temporary print statement indicating we are now inside the strength meter to calculate the actual strength/time it would take to relatively crack
        #print("special_length\n")
        
    #if(lower_length) >= 1:

        #temporary print statement indicating we are now inside the strength meter to calculate the actual strength/time it would take to relatively crack
        #print("lower_length\n")

    #if(upper_length) >= 1:

        #temporary print statement indicating we are now inside the strength meter to calculate the actual strength/time it would take to relatively crack
        #print("upper_length\n")

    #if(number_length) >= 1:

        #temporary print statement indicating we are now inside the strength meter to calculate the actual strength/time it would take to relatively crack
        #print("number_length\n")
        

    return

password = input("\nEnter in a password to test: ")

print("\n")
length_of_password(password)
check_for_special_characters(password)
check_for_lowercase(password)
check_for_uppercase(password)
check_for_numbers(password)
check_for_spaces(password)
check_common_pwd_list(password)
check_usage(password)

check_all_flags()
check_strength(password)



