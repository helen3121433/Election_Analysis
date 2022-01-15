print("Hello World")
age = 3.41
type(age)


5+2*3
8//5-3
8+22*2-4
16-3/2+7-1
3**3%5
5+9*3/2-4

(5+2)*3
(8//5)-3
8+(22*(2-4))
16-3/(2+1)-1
3**(3%5)
5+(9*3/2-4)
5+(9*3/(2-4))

counties = ["Arapahoe", "Denver", "Jefferson"]
# find the last item in counties list
print(counties[-1])

# find the second to last item in the list
print(counties[-2])

#fine total number of items in a list
len(counties)

# list[start : end] , 
# start -  refers to the index of first items in the slice, 
# end - is index making the end of the slice
# find first and second item form counties list . 

# Return ['Arapahoe','Denver']
counties[0:2]

#Return['Arapahoe']
counties[0:1]

# Return ['Arapahoe', 'Denver']
counties[:2]

# Return ['Denver', 'Jefferson']
counties[1:3]
counties[1:]

# Add item to the list - list.append()
counties.append("El Paso")

# Add item, select the location with an index - list.insert(index,obj)
# Return ['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
counties.insert(2, "El Paso")

#remove item from list
counties.remove("El Paso")

# pop() method can also remove the items at a given index from the list, then returns the removed item
# if "El Paso" is the fourth item in the list, then use index 3
# output will be 
# counties.pop(3)
# 'El Paso'
counties.pop(3)

# change element in the list
counties[2] = "El Paso"



# Tuples are simiplar to lists in python, but once you create a tuple, cannot be changed
# this means tuples are immutable: we can't add or remove items from them

# create an empty tuple
my_tuple = ()

#bhilt-in tuple() method
my_tuple = tuple()

counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
counties_tuple[1]

# get Arapahoe and Dever from counties_tuple list
counties_tuple[:2]
counties_tuple[:-1]

# Dictionary is an object that stores a collection of data. 
# Python dictionary has a key and a value, or key-value pairs
# word = key : definition = value
# {key:value}

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
# {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

# dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
counties_dict.items()

# dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
counties_dict.keys()

# dict_values([422829, 463353, 432438])
counties_dict.values()

# four ways to get the number of registed vote in Arapahoe country
counties_dict['Arapahoe']
counties_dict.get("Arapahoe")
print(counties_dict['Arapahoe'])
print(counties_dict.get("Arapahoe"))

# list of dictionaries

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})

# How many vote did you get?
my_votes = int(input("How many votes did you get in the elections?"))

# Total votes in the election
total_votes = int(input("What is the total votes in the election?"))

#calculate the percentage of votes you received
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes) + "% of the total votes.")


# if statement practice

counties = ["Arapahoe", "Denver" , "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# != not equal to
# == equal to

# if-else statement

temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the Ac.")
else:
    print("Open the windows.")

# else if  - elif


# in operator : returns True is a sequence with a secificed value is present in the object
#counties = ["Arapahoe","Denver","Jefferson"] if "Arapahoe" in counties: print("True") else: print("False")
#counties = ["Arapahoe","Denver","Jefferson"] if "El Paso" not in counties: print("True") else: print("False")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


# and, or, not

#Arapahoe or El Paso is not in the list of counties.
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# Arapahoe or El Paso is in the list of counties.
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


# While Loop
x = 0
while x<=5:
    print(x)
    x = x + 1

# For loop
for country in counties:
    print(country)

numbers = [0,1,2,3,4,"hi"]
for num in numbers:
    print(num)

for num in range(5):
    print(num)


# get key in dictory, for loop
for county in counties_dict.keys():
    print(county)

#values in dictionary, for loop
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

# for key,value in dictoionary_name.items()
#   print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#Arapahoe
#422829
#Denver
#463353
#Jefferson
#432438
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


# f string
# f'{}'
