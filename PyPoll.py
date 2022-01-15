
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# OPen the election results and read the file.

#with open(file_to_load) as election_data:
    #print the file object.
    #print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    # rea the file object with the reader function
    file_reader = csv.reader(election_data)

    #print each row in the csv file.
    #for row in file_reader:
     #   print(row)

    # print the header row.
    headers = next(file_reader)
    print(headers)

#using the open() function with the "w" mode we will warite data to the file
#outfile = open(file_to_save,"w")
#write some data to the file.
#outfile.write("Hello World")
#close the file
#outfile.close()

# using the with statement oepn the file as a text file.
#with open(file_to_save,"w") as txt_file:
    #write some data to the file
   # txt_file.write("end world")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    # or using txt_file.write("Arapahoe, Denver, Jefferson")

    #\n on next line(return, new line)
    #txt_file.write("\nhi\nbye")