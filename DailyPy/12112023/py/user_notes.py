#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:54:21 2023

@author: zhihaowang
"""

# Prompt the user for notes
user_notes = input("Enter your notes: ")

with open("user_log.txt", "a") as log_file:
    log_file.write(user_notes + "\n")
    
print("Notes have been logged.")

# "r" (read): This mode is used for reading from a file. It is the default mode if no mode is specified.

# "w" (write): This mode is used for writing to a file. If the file already exists, it will be truncated (emptied) before writing. If the file does not exist, a new file will be created.

# "a" (append): This mode is used for appending data to the end of a file. If the file does not exist, a new file will be created.