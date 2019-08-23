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
        self.extensionless_filename= ""

        self.slice_num=0
        self.blue_voltage=0
        self.UV_voltage =0
        self.display_time =0

        self.information_list = []
        self.remove_extension()
        self.extract_voltage()


    #This function will parse through a file and and return tuple containg the file number, the UV light voltage and the blue light voltage
    def remove_extension(self):
        period_index = len(self.original_filename)
        for index, c in reversed(list(enumerate(self.original_filename))):
            if (c == "."):
                period_index=index
                break
        self.extensionless_filename = self.original_filename[0:period_index]

    def extract_voltage(self):
        #split returns a list that seperates the file at the nunderscore.
        #exposure2_uv3.5_b2.3 would become ["exposure2, uv3.5, b2.3"]
        string_exposure_uv_blue_list = self.extensionless_filename.split("_")
        #This list stores slice num, UV voltage, blue voltage, and display time values
        EUB_values = [self.slice_num,self.UV_voltage,self.blue_voltage,self.display_time]
        #This loops through the string_exposure_uv_blue_list and takes the numerical values and stores it in the EUB list
        for outer_index, element in enumerate(string_exposure_uv_blue_list):
            for index, c in enumerate(element):
                if (c.isdigit()):
                    EUB_values[outer_index]=(float(element[index:]))
                    break
        #Sets the member variables declared in the constructor 
        self.slice_num=EUB_values[0]
        self.UV_voltage=EUB_values[1]
        self.blue_voltage=EUB_values[2]
        self.display_time =EUB_values[3]


#This function takes in a file path as an input, converts the filenames into the informative filename class, and outputs this as a list
def readfiles(path): 
    file_list =os.listdir(path)
    informative_filename_list = []
    for file in file_list:
        informative_filename_list.append[informative_filename(file)]
    return informative_filename_list







        
