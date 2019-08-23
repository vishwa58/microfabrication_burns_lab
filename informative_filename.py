#Created by Vishwa Nathan (vnathan@umich.edu)
#This file creates a class which will take in a file name pertaining to a specific DLP image.
#The filename will hold three pieces of information: the number of the image, the voltage for the blue light and the voltage for the UV light#
#The class then stores each piece of information in a seperate variable which can be accessed later


#USE FORMAT "ExposureN_UVX_BY.png" (see below for which part can be changed and which must be constant)
#In order for this class to work the filename it takes in must be saved as  EXPOSUREx_UVy_Bz.extension where NUM, UV, B and extension may be changed to anything but the values for the 
#slice num (x) and uv voltage (y) must be at the end of NUM and UV respectively and before the underscore. Blue voltage (z) must be at the end of B, but before the extension.

import os
import microfabrication_constant as MFC




class informative_filename:

    
    def __init__(self, file):
        self.original_filename = file       
    #properties below contain data regarding the slice number, the UV light voltage, the blue light voltage, and the time the image will be displayed 
    #on the computer. First the extension is removed from the original filename, then the extract_voltage method is run and a tuple
    #containing the light data is returned. The tuple is ordered as such: 1. slice_num, 2. UV_voltage, 3. blue_voltage, 4. display_time

    #These properties do not have setters, so they cannot be changed in the code itself. However, in the GUI, there will be an option to change these values
    #when the program is run


    @property
    def slice_num(self):
        return self.extract_voltage(self.remove_extension(self.original_filename))[0]
    @property
    def UV_voltage(self):
        return self.extract_voltage(self.remove_extension(self.original_filename))[1]
    @property
    def blue_voltage(self):
        return self.extract_voltage(self.remove_extension(self.original_filename))[2]
    @property
    def display_time(self):
        return self.extract_voltage(self.remove_extension(self.original_filename))[3]

    def __repr__(self):
        return self.original_filename

    #This function will parse through a file and and return tuple containg the file number, the UV light voltage and the blue light voltage
    def remove_extension(self, filename):
        period_index = len(filename)
        for index, c in reversed(list(enumerate(filename))):
            if (c == "."):
                period_index=index
                break
        return filename[0:period_index]

    def extract_voltage(self, filename):
        #split returns a list that seperates the file at the underscore.
        #exposure2_uv3.5_b2.3_t0.05 would become ["exposure2", "uv3.5", "b2.3", "0.05"]
        string_exposure_uv_blue_list = filename.split("_")
        #This list stores slice num, UV voltage, blue voltage, and display time values
        EUB_values = [0,0,0,0]
        #This loops through the string_exposure_uv_blue_list and takes the numerical values and stores it in the EUB list
        for outer_index, element in enumerate(string_exposure_uv_blue_list):
            for index, c in enumerate(element):
                if (c.isdigit()):
                    EUB_values[outer_index]=(float(element[index:]))
                    break
        #Sets the member variables declared in the constructor 
        return tuple(EUB_values)



#This function takes in a file path as an input, converts the filenames into the informative filename class, and outputs this as a sorted list
#by slice_num
def read_files(path): 
    file_list =os.listdir(path)
    informative_filename_list = []
    for file in file_list:
        if not file.startswith("."):
            informative_filename_list.append(informative_filename(file))
    informative_filename_list.sort(key = lambda file: file.slice_num)
    return informative_filename_list







        
