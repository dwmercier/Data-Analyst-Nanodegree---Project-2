from pandas import *
from ggplot import *
import numpy as np
from datetime import datetime


### Assign local environment variables and call function(s) if necessary
def main():

    # Set local directory for data files
    import os

    current_dir = os.getcwd()
    data_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2]) +'\\[Data]'

    # Assign path to local file(s)
    turnstile_weather = pandas.read_csv(data_dir + "\\turnstile_data_master_with_weather.csv")

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

    # Convert days of the week into integers
    convert_to_weekdays = turnstile_weather.DATEn.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    turnstile_weather.day_of_the_week = convert_to_weekdays.apply(lambda x: datetime.strftime(x, '%w'))

    # Group ENTRIESn_hourly by weekday and sum for each day
    daily_sum = turnstile_weather.ENTRIESn_hourly.groupby(turnstile_weather.day_of_the_week).sum()

    # Create a new dataframe with columns for day of the week and the total entries for that day of the week
    sum_by_weekday = pandas.DataFrame(
        {'Day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
         'Total Entries per Weekday': daily_sum}
         )
    # Plot bar chart showing total riders by weekday
    plot = ggplot(sum_by_weekday, aes(x='Day', y='Total Entries per Weekday')) +\
         geom_bar(stat='bar') +\
         ggtitle('Total Entries by Weekday') +\
         xlab('Day') +\
         ylab('Entries')

    return plot


# If running locally, call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()
