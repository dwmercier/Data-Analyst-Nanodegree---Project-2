import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Set matplotlib graph style
plt.style.use('fivethirtyeight')
font_1 = {'fontname':'Open Sans', 'size':'small'}

### Assign local environment variables and call function(s) if necessary
def main():
    
    # Set local directory for data files
    import os

    current_dir = os.getcwd()
    data_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2]) +'\\[Data]'

    # Assign path to local file(s)
    turnstile_weather = pd.read_csv(data_dir + "\\turnstile_data_master_with_weather.csv")

    # Print the histogram generated by the 'entries_histogram' function
    print(entries_histogram(turnstile_weather))


def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.

    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()

    Your histograph may look similar to bar graph in the instructor notes below.

    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms

    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''

    # Generate empty plot
    plt.figure()

    # Set cutoff to remove outliers from plot
    turnstile_weather[turnstile_weather.ENTRIESn_hourly>=6500]=6500

    # Generate and overlay histograms of ENTRIESn_hourly for rainy and non-rainy days
    turnstile_weather.ENTRIESn_hourly[turnstile_weather.rain == 0].hist(alpha=.75, label='No Rain',bins = 100) # your code here to plot a historgram for hourly entries when it is not raining
    turnstile_weather.ENTRIESn_hourly[turnstile_weather.rain == 1].hist(label='Rain', bins = 100) # your code here to plot a historgram for hourly entries when it is raining

    # Add title, labels and legend
    plt.xlabel('ENTRIESn_hourly', **font_1)
    plt.ylabel('Frequency', **font_1)
    plt.legend(['No Rain', 'Rain'])

    return plt


### Call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()
