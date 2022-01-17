# The data we need to retrieved.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

# Print the present time.
print("The time right now is ", now)

import csv

# Using dir() funciton, that will return all funcion available

# use dir() on csv module,  will return all funtion that can be use. 
# example, we have "reader" in one of function, we can use this funciton to read the csv file
dir(csv)

# use dir(), will return all functions available on that variable
# reduce, new, clear, copy, get, items, keys, pop, values....
dir({'Arapahoe': 422829, 'Denver':463353, 'Jefferson':432438})

# the dir() on data type like str, will return all attributes and method that can be use with str data
# such as count, join, loser, split, replace,rfind,rindex....
dir(str)

dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)

# dir(datetime)
dir(dt)

# import random
# import numpy

# General format for opening a file is:
# file_variable = open(filename, mode)
# file_variable is name of the varaible that reference the file object
# filename is a string specifying the name of the file
# mode is a string specifiy the mode for reading or writing the file object. possible modes are:
    # "r": open a file to be read
    # "w": open a file to write to it. This will overwrite and existing file and create a file if one does not aleady exist
    # "x": open a file for exclusive creation. if the file does not exist, it will not create one
    # "a": open a file to append data to an existing file. If a file does not exist, it creates one. IF a file has been created data will be added to the file
    # "+": open a file for reading and writing

import csv
# Assign a variable for the file to load and the path
# telling the computer to get eletion_result.csv file that is located in "resources folder"
file_to_load = 'Resources/election_results.csv'


# Next, open file_to_load, with open() funciton. using "r" mode to read the file.
# Then we'll print the filename object.
# After reading the file, close the file with close() function.
# In between the opeing and closing of the fille, is where we will read the data nad perform our analysis

# Open the election result and read the file
election_data = open(file_to_load,'r')

# to do: perform analsyis.

#close the file
election_data.close()

# another way to read and write to a file without needing to use the open() and close() function everytime. 
# we simply replace open() function, use [with] statement
# [with] statement opens file and ensures proper acquisition or ealse of any data without having to close the file,
# and to ensure that the data isn't lost or corrupted.

# Open the election results and read the file
with open(file_to_load) as election_data:
    # to do: perform analysis.
    print(election_data)

# import os module allow us to internact with our operation system.
import os
dir(os)

# Submodule os.path allow us to access file on a different operation system
dir(os.path)

# join() unction joins our file patch components together when they are provided as separate strings;
# then return a direct path with appropriate operating system separator,
# forward slash for macOS or backward slash for Windows
 # macOS uses the forwards-slash: /
 # Windows use the backslas: \