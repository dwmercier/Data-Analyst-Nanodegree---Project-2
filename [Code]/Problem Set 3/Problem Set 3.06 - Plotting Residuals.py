import numpy as np
import scipy
import matplotlib.pyplot as plt

### Assign local environment variables and call function(s) if necessary
def main():

    # Set local directory for data files
    import os

    current_dir = os.getcwd()
    data_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2]) +'\\[Data]\\'

    os.chdir(data_dir)

    # Assign path to local file(s)
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    
    # Print the plot generated by the 'plot_residuals' function
    print(plot_residuals(turnstile_weather, predictions))



def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''

    # Generate empty plot
    plt.figure()

    # Generate histogram of residuals
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins = 75)

    # Add title, labels and legend
    plt.title('ENTRIESn_hourly Regression Residuals')
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')

    return plt


### Call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()

