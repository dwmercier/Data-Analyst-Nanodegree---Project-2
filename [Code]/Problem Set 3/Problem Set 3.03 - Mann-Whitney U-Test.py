import numpy as np
import scipy
import scipy.stats
import pandas as pd


### Assign local environment variables and call function(s) if necessary
def main():
    
    # Set local directory for data files
    import os
    
    current_dir = os.getcwd()
    data_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2]) +'\\[Data]'

    # Assign path to local file(s)
    turnstile_weather = pd.read_csv(data_dir + "\\turnstile_data_master_with_weather.csv")
   
    # Print the result of the 'mann_whitney_plus_means' function
    results = mann_whitney_plus_means(turnstile_weather)
    print('Mann-Whitney U test results:')
    print('with_rain_mean = ' + str(results[0]))
    print('without_rain_mean = ' + str(results[1]))
    print('U = ' + str(results[2]))
    print('p = ' + str(results[3]))


def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data.

    You will want to take the means and run the Mann Whitney U-test on the
    ENTRIESn_hourly column in the turnstile_weather dataframe.

    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain

    You should feel free to use scipy's Mann-Whitney implementation, and you
    might also find it useful to use numpy's mean function.

    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html

    You can look at the final turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''

    ### YOUR CODE HERE ###

    # Assign ENTRIESn_hourly entries to variables according to rain status
    with_rain = turnstile_weather.ENTRIESn_hourly[turnstile_weather.rain == 1]
    without_rain = turnstile_weather.ENTRIESn_hourly[turnstile_weather.rain == 0]

    # Calculate individual means of entries with and without rain
    with_rain_mean = np.mean(with_rain)
    without_rain_mean = np.mean(without_rain)
    
    # Calculate Mann-Whitney U results and assign to respective variables
    mannwhitney_results = scipy.stats.mannwhitneyu(with_rain, without_rain)
    U, p = mannwhitney_results[0], mannwhitney_results[1]

    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader

### Call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()