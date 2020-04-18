# Author: Joshua Barnes
# Purpose: To display different crime and where they take place across the city of Chicago
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Import Libraries
import pandas as pd
import os
import numpy as np
#import shapefile as shp
import geopandas as gpd
#import seaborn as sns
import descartes as dsc
import matplotlib.pyplot as plt

#################################################################################################################################################################################################################################
# This function gets all of the City crime data from a file, and does some mild restructuring of the data
def GET_DATA():
#----------------------------GET THE DATA--------------------------------------------------------------------------------------------------------------------------
    # Get the current working directory
    os.getcwd()
    # Change the working directory to the one with the necessary files
    os.chdir("/Users/joshuabarnes/Documents/Python Projects/CRIME__Project")

    # Read in the CSV file
    READ_CRIME_CSV = pd.read_csv("Chicago_Crimes_2012_2017.csv", sep=",", quotechar='"', encoding='utf8')

    # Create a variable that controls how many rows will be shown
    MAX_ROW_SEEN = 101

    # We don't want all of the data in the file, so we will select the specific data that we want:

    # 1 Get the 'Date' data:
    DATE_DATA = READ_CRIME_CSV['Date'][1:MAX_ROW_SEEN]
    # 2 Get the 'Year' data:
    YEAR_DATA = READ_CRIME_CSV['Year'][1:MAX_ROW_SEEN]
    # 3 Get the case 'ID' data:
    CASE_ID_DATA = READ_CRIME_CSV['ID'][1:MAX_ROW_SEEN]
    # 4 Get the "Case Number" data:
    CASE_NUM_DATA = READ_CRIME_CSV['Case Number'][1:MAX_ROW_SEEN]
    # 5 Get the 'Ward' information:
    CASE_WARD_DATA = READ_CRIME_CSV['Ward'][1:MAX_ROW_SEEN]
    # 6 Get the 'Block' data:
    BLOCK_DATA = READ_CRIME_CSV['Block'][1:MAX_ROW_SEEN]
    # 7 Get the 'Arrest' data:
    ARREST_DATA = READ_CRIME_CSV['Arrest'][1:MAX_ROW_SEEN]
    # 8 Get the 'Domestic' data:
    DOMESTIC_DATA = READ_CRIME_CSV['Domestic'][1:MAX_ROW_SEEN]
    # 9 Get the 'Primary Type' data:
    PRIMARY_TYPE_DATA = READ_CRIME_CSV['Primary Type'][1:MAX_ROW_SEEN]
    # 10 Get the 'Description' data:
    DESCRIPTION_DATA = READ_CRIME_CSV['Description'][1:MAX_ROW_SEEN]
    # 11 Get the 'Latitude' data:
    LATITUDE_DATA = READ_CRIME_CSV['Latitude'][1:MAX_ROW_SEEN]
    # Get the 'Longitude' data:
    LONGITUDE_DATA = READ_CRIME_CSV['Longitude'][1:MAX_ROW_SEEN]

    # 11 Concatenate (put them next to each other) the columns generated above
    COMBINED_DATA_FRAME = pd.concat([DATE_DATA, YEAR_DATA, CASE_ID_DATA, CASE_NUM_DATA, CASE_WARD_DATA, BLOCK_DATA,
                                    ARREST_DATA, DOMESTIC_DATA, PRIMARY_TYPE_DATA, DESCRIPTION_DATA, LATITUDE_DATA, LONGITUDE_DATA], axis=1)

    # Format the display so that all of the columns and rows are able to be shown:
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', None)

    # Make the index of the rows start with 0 (makes it easier to access specific cells)
    COMBINED_DATA_FRAME.index = np.arange(0, len(COMBINED_DATA_FRAME))

    # Print out the dataframe:
    #print("\n", COMBINED_DATA_FRAME)

    # Check the data type for COMBINED_DATA_FRAME
        #print('\nCOMNBINED_DATA_FRAME type is: ', type(COMBINED_DATA_FRAME))

    # Prints out the value of a specific cell
    #print("\n", COMBINED_DATA_FRAME.iloc[0, 0])

    # Return COMBINED_DATA_FRAME  so that it can be called by other functions
    return COMBINED_DATA_FRAME

GET_DATA() # GET_DATA() END
#################################################################################################################################################################################################################################

# This function is to create the map. The data from GET_DATA() will be loaded into the map later
def GET_MAP():

    # Get the path of the shapefile (on my local machine)
    map_path = "//Users//joshuabarnes//Documents//Python Projects//CRIME__Project//Boundaries - ZIP Codes//geo_export_4cda2e7d-7d1d-4f72-9fab-575df38eef8d.shp"
    # Read in the Shapefile
    read_in_map = gpd.read_file(map_path)

    # Return read_in_map so that it can be called by other functions
    return read_in_map

GET_MAP() # GET_MAP() END
'''
# This function asks the user the specific data that they would like to filter on and view
def GET_FILTER_DATA():
    COMBINED_DATA_FRAME = GET_DATA()

    # Ask the user what type of data that they would like to filter on
    print('\n')
    # Make a counter to put a umber next to each columns
    counter = 1
    # Loop and print out each possible column name for the user to filter on
    for col in COMBINED_DATA_FRAME.columns:
        print(counter, '-', col)
        counter = counter + 1

    # Ask the user what specific column they would like to filter on
    crime_type = input("\nSelect the number that corresponds to the specific data that you would like to filter on: ")

    # If the User Chooses 'Date', Display all possible dates:
    counter = 1
    if crime_type == '1':
        # Create a variable that holds all of the unique values in the specific column that the user chose
        unique_element = COMBINED_DATA_FRAME.Date.unique()
        # Print the unique values of the specific column on a new line  for each value
        for word in unique_element:
            print(counter, '-',word)
            counter = counter + 1
    print("\nYou selected Date, now chose the specific date that you would like to filter on: ")

    # If the user chooses 'Year', Display all of the unique values in the specific column that the user chooses
    if crime_type == '2':
        unique_element = COMBINED_DATA_FRAME.Year.unique()
        # Print the unique values 
        for word in unique_element:
            print(counter, '-', word)
            counter = counter + 1
    print("\nYou selected Year, now choose the specific year that you would like to filter on: ")

    # if th euser chooses 'ID', Display all of the unique values in the specific column that the user chooses
    if crime_type == '3':
        unique_element = COMBINED_DATA_FRAME.unique()
        # Print unique values
        for word in unique_element:
            print(counter, '-', word)
            counter = counter + 1
    print("\nYou selected ID, now enter the specific ID that you would like to search for: ")


GET_FILTER_DATA() # DISPLAY_DATA() END
'''

#################################################################################################################################################################################################################################
# This function uses the map from GET_MAP() and plots points on it retrieved from GET_DATA()

def DISPLAY_DATA_POINTS():
    read_in_map = GET_MAP()
    COMBINED_DATA_FRAME = GET_DATA()

    # Get the Latitude ang Longitude of each crime from COMBINED_DATA_FRAME
    GET_LAT_LONG = gpd.GeoDataFrame(COMBINED_DATA_FRAME, geometry=gpd.points_from_xy(COMBINED_DATA_FRAME.Longitude,
                                                                                     COMBINED_DATA_FRAME.Latitude))

    # Establish the colors of the shapfile
    ax = read_in_map.plot(color='blue', edgecolor='black')

    # Set the color of the plot (based on Lat. and Long.) a color, and plot the shapefile
    GET_LAT_LONG.plot(ax=ax, color='red')

    # Show the shapefile on-screen
    plt.show()

    # Print out the data from COMBINED_DATA_FRAME that is being accessed from GET_DATA():
    print(COMBINED_DATA_FRAME)

DISPLAY_DATA_POINTS()

#################################################################################################################################################################################################################################
