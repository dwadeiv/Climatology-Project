# David Wade
# Section 201
# Climatology 
# This program itterates through 230 different files from the years 1900-2014
# that have the temperature and percipitation data from stations across the globe.
# This program is used to reduce the 85,794 rows of data into a new file that
# contains reduced data in the form of maxes, mins, sums, and averages. 
# These values are then used to create various graphs filled with different data sets
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors 
import time

class WeatherData: 
    year = 0
    lat = 1
    long = 2 
    annual_min = 3 
    annual_max = 4 
    annual_avg = 5 
    annual_sum = 6




    
    
"""
 I wrote this funnction and it works, but I never call it because I did not need it.
 This was done due to it being a subtask.
"""
def row_count():
    infile = open("air_temp.1900" , "r")
    count = 0
    for line in infile:
        count += 1 
    infile.close()
    return (count)






"""
 This function first creates an empty 3-D array with year count, row count, and data types.
 Then iterates through 115 files then creating the data into a list which is then created 
 into a numpy array where calculations are made to find the max, min, sum, and mean of each 
 row. This new data is then filled into the inital 3-D array as the third demnsion.
"""
def read_data(name_base_temp):
    data_array = np.zeros((115, 85794, 7))
    for i in range(1900,2015):
        filename_temp = name_base_temp + str(i) 
        file_obj = open(filename_temp , "r")
        j = 0
        for row in file_obj:
            row1 = row.split()
            row_values = row1[2:]
            row_values = np.array(row_values, dtype = np.float(64))
            maximum_value = np.max(row_values)
            minimum_value = np.min(row_values)
            mean_value = np.mean(row_values)
            sum_value = np.sum(row_values)
            lat = row1[0]
            long = row1[1]
            reduced_data_arr = np.array([i,lat,long,minimum_value,maximum_value,mean_value,sum_value])
            data_array[i-1900, j, :] = reduced_data_arr
            j += 1
        file_obj.close()
    return(data_array)






"""
 This function takes the newly reduced data and saves them into two separate numpy
 files that can be called again. One file is for Temperature and the other is for Percipitation.
"""
def new_file(x,y):
    np.save("Temp_Reduced_Data", x)
    np.save("Precip_reduced_Data", y)






"""
 This function takes the reduced temperature data, and then calls the annual_global_avg_temp
 function in order to obtain the average of all the temp averages for each year. It then
 uses that data to plot the average global temperature for each year
"""  
def global_annual_mean_temp(temp_data):
    temp = annual_global_avg_temp(temp_data)
    year = np.arange(1900,2015)
    plt.figure(figsize=(15,10))
    plt.plot(year,temp)
    plt.xlabel("Year")
    plt.ylabel("Temp in deg celcius")
    plt.title("Time series of global annual mean surface temperature from 1900 to 2014")
    plt.show()
    plt.savefig("mean_temp.pdf")






"""
 This function takes the sum of the global annual percipitation in inches, and then plots
 a graph over the time interval of 1900 - 2014
"""        
def total_annual_precipitation(precip_data):
    annual_total = precip_data[:, :, 6]
    global_precip_arr = np.array([])
    for file in annual_total:
        global_annual_sum = np.sum(file)
        global_precip_arr = np.append(global_precip_arr, global_annual_sum)      
    year = np.arange(1900,2015)
    plt.figure(figsize=(15,10))
    plt.plot(year,global_precip_arr)
    plt.xlabel("Year")
    plt.ylabel("Precipitation in I")
    plt.title("Time series of global annual total precipitation from 1900 to 2014")
    plt.show()
    plt.savefig("annual_precip.pdf")




 
    
"""
 This function solely retrieves averages all of the mean values for each year, then 
 creates an array filled with all of the new average values
""" 
def annual_global_avg_temp(temp_data):
    annual_means = temp_data[:, :, 5]
    global_temp_arr = np.array([])
    for file in annual_means:
        global_annual_mean = np.mean(file)
        global_temp_arr = np.append(global_temp_arr, global_annual_mean)
    return(global_temp_arr)






"""
 This function is called in the anomoly functions and returns the anomoly between
 the annual average and the average over a certain time interval. These values are used 
 as the values for those graphs' y-axis
"""   
def y_axis_temp_anm(all_averages, total_average):
    y_axis = []
    for average in all_averages:
        point = average - total_average
        y_axis.append(point)
    return(y_axis)
    




    
"""
 This function uses a calculated reference value from the time interval 1900-2014
 in order to graph the anomalies between the anual averages and the refence value which
 is the average of the annual averages. Aditiponally, this function does not have array operations
 and only uses for loops to retrieve the needed data. 
"""  
def temp_anm_loops(temp_data):
    start = time.time()
    all_averages = annual_global_avg_temp(temp_data)
    total = 0
    for average in all_averages:
        total += average
    total_average = (total/115)
    y_axis = y_axis_temp_anm(all_averages, total_average)
    year = np.arange(1900,2015)
    plt.figure(figsize=(15,10))
    plt.plot(year,y_axis)
    plt.xlabel("Year")
    plt.ylabel("Temp in deg celcius")
    plt.title("Time series of global temperature anomalies with respect to 1900 to 2014 reference value: -4.99853125096")
    plt.show()
    stop = time.time()
    print("Time taken to run function: " + str(stop-start))
    plt.savefig("temp_anomalies_1900_2014.pdf")
 
    
    
    
    

"""
 This function uses a calculated reference value from the time interval 1951-1980
 in order to graph the anomalies between the anual averages and the refence value which
 is the average of the annual averages. 
"""      
def temp_anm_arr(temp_data):
    start = time.time()
    all_averages = annual_global_avg_temp(temp_data)
    sum_averages = np.sum(all_averages[51:81])
    total_average = (sum_averages/30)
    y_axis = y_axis_temp_anm(all_averages, total_average)
    year = np.arange(1900,2015)
    plt.figure(figsize=(15,10))
    plt.plot(year,y_axis)
    plt.xlabel("Year")
    plt.ylabel("Temp in deg celcius")
    plt.title("Time series of global temperature anomalies with respect to 1951 to 1980 reference value: -5.17919068091")
    plt.show()
    stop = time.time()
    print("Time taken to run function: " + str(stop-start))
    plt.savefig("temp_anomalies_1951_1980.pdf")






"""
 This function takes in teh reduced percipitaion data as its only paramter, it then 
 averages all of the averages to come up with one global average for each year. It then 
 finds and plots each rate of change between each global average over the interval of 
 1900-2014. 
"""
def rate_of_change_mean_precip(precip_data):
    data = precip_data[:,:,5]
    yearly_averages = []
    for average in data:
        data = np.mean(average)
        yearly_averages.append(data)
    y_axis = []
    for i in range(114):
        rate_of_change = yearly_averages[i+1] - yearly_averages[i]
        y_axis.append(rate_of_change)
    year = np.arange(1900,2014)
    plt.figure(figsize=(15,10))
    plt.bar(year,y_axis)
    plt.xlabel("Year")
    plt.ylabel("rate of change in mean precipitation ml/year")
    plt.title("Rate of change in global annual mean precipitation between 1900 and 2014")    
    plt.show()
    plt.savefig("change_precip.pdf")






"""
 This function takes in 3 parameters, the reduced temp data, given year, and given
 bin-size. It then creates a frequency histogram, with the given bin_size, of the 
 average minimum temperatures for that year.
"""    
def hist_min_temp(temp_data,year,bin_size):
    data = temp_data[year-1900,:,3]
    plt.figure(figsize=(15,10))
    plt.hist(data,bins = bin_size)
    plt.xlabel("Min temperature in deg Celcius")
    plt.ylabel("No. of locations with min temperature of a particular value")
    plt.title("Histogram of min temperatures as recorded at all locations during year " + str(year))
    plt.show()
    plt.savefig("min_temps_everywhere.pdf")






"""
 This function creates a scatter plot with the x-axis being latitude and the y-axis
 being longitude. It uses the coordinates for each weather station across the globe to
 to formulate a graph that looks like the continents. It then colorizes the plot points
 by the mean precipitation for that weather station. The end result is a heat map 
 of the globe based on mean percipitation.
"""    
def heat_map_precip(precip_data,year):
    mean_precip_data = precip_data[year-1900,:,5]
    lat_data = precip_data[year-1900,:,1]
    long_data = precip_data[year-1900,:,2]
    plt.figure(figsize=(15,10))    
    plt.scatter(lat_data, long_data, c=(mean_precip_data), norm=colors.LogNorm())
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.title("Mean precipitation in ml, " + str(year))
    plt.colorbar()
    plt.show()
    plt.savefig("heat_map_precip_2014.pdf")






"""
 This function creates a scatter plot with the x-axis being latitude and the y-axis
 being longitude. It uses the coordinates for each weather station across the globe to
 to formulate a graph that looks like the continents. It then colorizes the plot points 
 by the mean of all the averages a certain weather station has in the given time interval.
"""
def heat_map_temp(temp_data, year_1, year_2):
    lat_data = temp_data[0,:,1]
    long_data = temp_data[0,:,2]   
    mean_temp = []
    for i in range(85794):
        data = temp_data[(year_1-1900):(year_2-1900),:,5][:,i]
        mean_temp.append(np.mean(data))
    plt.figure(figsize=(15,10))
    plt.scatter(lat_data, long_data, c=mean_temp)
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.title("Mean temperature in degrees celcius averaged over the period " + str(year_1) + " - " + str(year_2))
    plt.colorbar()
    plt.show()
    plt.savefig("heat_map_temp_1920_1939.pdf")
    
 
    
    
    
    
"""   
 This function will take the user's choice and will keep asking for an input until
 A valid answer or the user inputs a 0. After the input requirement is met, it will 
 then return their input in order for the program to display the correct data 
"""
def get_menu_choice():
    temp_data = np.load("Temp_Reduced_Data.npy")
    precip_data = np.load("Precip_reduced_Data.npy")
    choice = input("0: Exit" + "\n1: Global annual mean surface temperature" + "\n2: Global total annual precipitation" + "\n3: Global surface temperature anomalies (loops)" + "\n4: Global surface temperature anomalies (arrays)" + "\n5: Rate of change in mean precipitation" + "\n6: Histogram of minimum temperatures at all locations in a given year" + "\n7: Heat map of mean annual precipitation for a given year" + "\n8: Heat map of mean annual temperature for a given time period" + "\n9: Extra credit" + "\n" +"\n> ")
    end = False
    while end == False:
        if choice != str(0) and choice != str(1) and choice != str(2) and choice != str(3) and choice != str(4) and choice != str(5) and choice != str(6) and choice != str(7) and choice != str(8) and choice != str(9):
            choice = input("0: Exit" + "\n1: Global annual mean surface temperature" + "\n2: Global total annual precipitation" + "\n3: Global surface temperature anomalies (loops)" + "\n4: Global surface temperature anomalies (arrays)" + "\n5: Rate of change in mean precipitation" + "\n6: Histogram of minimum temperatures at all locations in a given year" + "\n7: Heat map of mean annual precipitation for a given year" + "\n8: Heat map of mean annual temperature for a given time period" + "\n9: Extra credit" + "\n" +"\n> ")
            end = False
        elif int(choice) == 0:
            print("")
            end = True
        elif int(choice) == 1:
            global_annual_mean_temp(temp_data)
            end = True
        elif int(choice) == 2:
            total_annual_precipitation(precip_data)
            end = True
        elif int(choice) == 3:
            temp_anm_loops(temp_data)
            end = True
        elif int(choice) == 4:
            temp_anm_arr(temp_data)
            end = True
        elif int(choice) == 5:
            rate_of_change_mean_precip(precip_data)
            end = True
        elif int(choice) == 6:
            year = int(input("What year? "))
            bin_size = int(input("What bin size? "))
            hist_min_temp(temp_data,year,bin_size)
            end = True
        elif int(choice) == 7:
            year = int(input("What year? "))
            heat_map_precip(precip_data,year)
            end = True
        elif int(choice) == 8:
            year_1 = int(input("This heat map requires a given time period. What year would you like to start? (1900-2014) "))
            year_2 = int(input("Until what year would you like to make your time period? (Up until 2014) "))
            heat_map_temp(temp_data, year_1, year_2)
            end = True
        elif int(choice) == 9:
            print("")
            end = True
      





def main():
    
    """
    Un-comment the following code if you do not have the reduded files saved
    """     
    name_base_temp = "air_temp."
    name_base_precip = "precip."
    x = read_data(name_base_temp)
    y =  read_data(name_base_precip)
    new_file(x,y)
    
    get_menu_choice()
    
if __name__ == '__main__':
    main()