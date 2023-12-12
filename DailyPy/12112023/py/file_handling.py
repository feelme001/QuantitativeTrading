#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:50:41 2023

@author: zhihaowang
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file!\n")
    file.write("Python is fantastic!\n")
    
# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
    
from datetime import datetime

current_time = datetime.now()

timestamp_filename = current_time.strftime("%Y%m%d_%H%M%S")
timestamp_message = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Construct the file name with the timestamp
file_name = f"log_{timestamp_filename}.txt"

message = "This is a message with a timestamp."

formatted_message = f"{timestamp_message}: {message}"

with open(file_name, "a") as file:
    file.write(formatted_message + "\n")