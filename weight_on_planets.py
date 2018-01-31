# This is a comment.  Python will ignore these lines (starting with #) when running
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)
import math as ma
from sys import argv

"""
filename must follow exact format example
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

for each in infile:
	line = each.split(";  ")
	listfile.append(line)
infile.close()

def traverse(o, tree_types=(list, tuple)):
	#allows to iterate through list of lists
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o

def number_extraction(data, list):
	#extracts floating values and adds them to a list
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

number_extraction(listfile, numlist)
build_table(listfile,numlist)

#abstract calculations
p = planet.lower()
m = float(mass) # mass will be in kg
alt = float(altitude) # altitude will be in meters
r = radius_table[p] * 1000 # radius will be in meters
d = density_table[p] * (100 ** 3) / (1000) # density will be in 
# kg / m^3
planet_volume = 4 / 3 * (r ** 3) * ma.pi # volume is in m^3
planet_mass = planet_volume * d  # kg
explorer_force = (6.674e-11) * planet_mass * m / ((alt + r) ** 2) # Newtons
grav_accel = explorer_force / m 

print planet_mass
print explorer_force
print grav_accel




	






