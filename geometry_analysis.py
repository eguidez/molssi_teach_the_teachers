"""
Geometry_analysis.py
This module contains the geometry analysis project.
"""
import os
import numpy
import sys

def open_xyz(input_file):
    """ This function opens input_file which is a .xyz file.
    Output is atom symbols and atom coordinates and atom number"""
    data = numpy.genfromtxt(fname = input_file, skip_header=2, dtype='unicode')
    symbols = data[:,0]
    atom_coord_string = data[:,1:4]
    coordinates = atom_coord_string.astype(numpy.float)
    atom_num = len(data)
    return symbols, coordinates, atom_num

def bond_check(distance, minimum_length=0, maximum_length=1.5):
    """This function checks if the distance between two atoms is between minimum_length and maximum_length
    If distance is between minimum and maximum length, return value true else returns false
    Defaults are minimum_length=0 and maximum_length=1.5"""
    if distance < 0:
        raise ValueError(F"Distance of ({distance}) is less that 0. Check your input")
    if distance < maximum_length and distance > minimum_length :
        value = True
    else:
        value = False
    return value

def calculate_distance(atom1_coord, atom2_coord) :
    """This function takes the coordinates of two atoms and calculates the distance between them
       Input:coordinates
       Output:Distance"""
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    distance = numpy.sqrt((x_distance**2)+(y_distance**2)+(z_distance**2))
    return distance


if __name__ == "__main__":
    print(F"Running {sys.argv[0]}")
    #bond_check(-5)
    if len(sys.argv) < 2:
        raise NameError("Incorrect input. Please specify an xyz file to be analyzed")
    water_file_path = sys.argv[1]
    water_symbols,water_coordinates,water_atom_num = open_xyz(water_file_path)
    for i in range(0,int(water_atom_num)):
        for j in range(0,int(water_atom_num)):
            if i < j:
                bond_length_12 = calculate_distance(water_coordinates[i], water_coordinates[j])
                if bond_check(bond_length_12) == True:
                    print(F'{water_symbols[i]} to {water_symbols[j]} : {bond_length_12:0.3f}')
