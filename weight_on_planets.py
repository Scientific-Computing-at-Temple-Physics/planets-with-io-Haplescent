# This is a comment.  Python will ignore these lines (starting with #) when running
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)
import math as ma
from sys import argv

"""
filename must follow example format
each item must be separated with a ;
Mercury;  2439.7 km;  5.427 g/cm^3;
planet can be lower or uppercase
altitude must be in meters
explorer mass must be in kilograms
"""
script, filename, planet, altitude, mass = argv

infile = open(filename, "r")
listfile = []
radius_table = {}
density_table = {}
numlist = []

def file_list(file, list):
	#This function will assign items between a ; in an opened file
	# and assign them to a list
	for each in file:
		line = each.split("; ")
		list.append(line)
	file.close()

def traverse(o, tree_types=(list, tuple)):
	#This traverse generator function can be used to iterate over all the values
	#from Jeremy Banks on stack_overflow
	#https://stackoverflow.com/questions/6340351/python-iterating-through-list-of-list
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o

def number_extraction(data, list):
	#extracts floating values and adds them to a list
	#from jmnas on stack_overflow
	#https://stackoverflow.com/questions/4289331/python-extract-numbers-from-a-string
	for each in traverse(data):
		for t in each.split():
			try:
				list.append(float(t))
			except ValueError:
				pass

def build_table(data1, data2):
	#builds a directory where data1 is the call and data2 is
	#the response
	x = 1
	while x != len(data1):
		radius_table[data1[x][0].lower()] = data2[2 * x - 2]
		density_table[data1[x][0].lower()] = data2[2 * x - 2 + 1]
		x = x + 1
	else:
		return "Built radius table"

file_list(infile, listfile)
number_extraction(listfile, numlist)
build_table(listfile,numlist)

#abstract calculations
p = planet.lower()
m = float(mass) # mass will be in kg
alt = float(altitude) # altitude will be in meters
r = radius_table[p] * 1000 # radius will be in meters
d = density_table[p] * (100 ** 3) / (1000) # density will be in 
# kg / m^3
planet_volume = 4.00 / 3.00 * (r ** 3) * ma.pi # volume is in m^3
planet_mass = planet_volume * d  # kg
explorer_force = (6.674 * 10 ** (-11)) * planet_mass * m / ((alt + r) ** 2) # Newtons
grav_accel = explorer_force / m 

print explorer_force
print grav_accel





	






