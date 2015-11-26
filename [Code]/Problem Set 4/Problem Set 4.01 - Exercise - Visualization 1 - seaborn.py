import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime
from matplotlib import pyplot as plt


### Assign local environment variables and call function(s) if necessary
def main():

    # Set local directory for data files
    import os

    current_dir = os.getcwd()
    data_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2]) +'\\[Data]'

    # Assign path to local file(s)
    turnstile_weather = pd.read_csv(data_dir + "\\turnstile_data_master_with_weather.csv")

    # Change font used by Seaborn
    sns.set(font="Open Sans")

    # Print the ouput of the 'plot_weather_data' function
    print(plot_weather_data(turnstile_weather))


def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    # Convert days of the week into integers in the turnstile_weather dataframe
    convert_to_weekdays = turnstile_weather.DATEn.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    turnstile_weather['day_of_the_week'] = convert_to_weekdays.apply(lambda x: datetime.strftime(x, '%w'))

    # Create dataframe
    heatmap_columns = turnstile_weather[['ENTRIESn_hourly', 'Hour', 'day_of_the_week']]

    # Group ENTRIESn_hourly by weekday
    grouped_by_weekday = heatmap_columns.groupby(heatmap_columns.day_of_the_week)

    # Create new dataframe for grouped columns
    ridership_heatmap = pd.DataFrame()

    # Group columns by hour and take the mean
    for k, group in grouped_by_weekday:
        ridership_heatmap[k] = group.groupby(group.Hour).mean()

    # Rename day columns to named days of the week
    weekday_names = {
        '0':'Sunday',
        '1':'Monday',
        '2':'Tuesday',
        '3':'Wednesday',
        '4':'Thursday',
        '5':'Friday',
        '6':'Saturday'
         }

    ridership_heatmap = ridership_heatmap.rename(columns=weekday_names)

    # Plot the heatmap
    plot = sns.heatmap(ridership_heatmap, annot=True,  fmt='.0f', linewidths=.5, cmap = "Blues")

    plt.xlabel('Day of the Week')
    plt.ylabel('Time Period (24 hr. format)')

    return plot


# If running locally, call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()


