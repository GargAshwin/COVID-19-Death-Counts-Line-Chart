import matplotlib.pyplot as plt
import numpy as np
import csv

"""
Takes data in csv into a list. The list is a 2d array with each row being each row within the csv file. This data 
comes directly from the CDC: Centers for Disease Control and Prevention. The csv file comes from this link 
(under download-data section): "https://covid.cdc.gov/covid-data-tracker/#trends_weeklydeaths_select_00". However, I made
a more summarized csv file from this data known as "data.csv". The data is largely the same, its just more condensed and
summarized.  
"""
def load_data(filename):
    myList = []
    with open(filename) as data:
        data = csv.reader(data, delimiter=',')
        next(data) #skip header
        for row in data:
            myList.append(row)
    return myList

#Gets all the death counts from Covid-19 for each month since 2021 from the csv file and puts those values into a list
def get_death_counts():
    data = load_data('data.csv')
    death_counts = []
    for row in data[2:]: #skip header and title of data set
        death_counts.append(int(row[2])) #index 2 of the row gives the death count of each row
    return death_counts

#Gets all the dates from the csv file and puts them into a list
#All dates are strings with the format 'year-month'
def get_dates():
    data = load_data('data.csv')
    dates = []
    for row in data[2:]: #skip header and title of data set
        d = row[0] + '-' + row[1] #index 0 of the row gives the year and index 1 of the row gives the month
        dates.append(d)
    return dates

#Labels the title and axes of the line graph
def load_Graph_Axes_Titles():
    plt.title("US Deaths Counts from Pneumonia, Influenza, or COVID-19 Over Time")
    plt.ylabel("Death Counts (#)")
    plt.xlabel("Dates (Year-Month)")

#Loads various features of the line graph (more info below)
def load_Graph_Features(death_counts, dates):
    plt.ylim(-5000, max(death_counts) + 10000)
    plt.axhline(y = 0, color = 'c', linestyle = '--')
    plt.gcf().autofmt_xdate()
    tick_positions = np.arange(len(dates))
    plt.xticks(tick_positions, dates, rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()

#Labels the specific death count for the first month, highest month, and most recent month, to improve data visualization
def label_Graph_Highlights(death_counts):
    start_x_value = -0.6;
    plt.annotate(f'({death_counts[0]})', (0, death_counts[0] + 2000),
                 ha='center', color = 'b')
    plt.annotate(f'({death_counts[12]})', (12, death_counts[12] + 2000),
                 ha='center', color = 'b')
    plt.annotate(f'({death_counts[52]})', (52, death_counts[52] + 2000),
                 ha='center', color = 'b')

#This function Loads the graph or displays it to the screen
def load_graph(death_counts, dates):
    plt.figure(figsize=(16, 8))
    load_Graph_Axes_Titles()
    plt.plot(dates, death_counts, marker='o', linestyle='--', color='r')
    load_Graph_Features(death_counts, dates)
    label_Graph_Highlights(death_counts)
    plt.show()

death_count = get_death_counts()
dates = get_dates()
load_graph(death_count, dates)
