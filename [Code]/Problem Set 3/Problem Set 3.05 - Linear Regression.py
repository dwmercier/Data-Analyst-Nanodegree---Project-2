import numpy as np
import pandas as pd
import statsmodels.api as sm
from datetime import datetime


"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""


### Assign local environment variables and call function(s) if necessary
def main():

    # Set local directory for data files
    import os

    current_dir = os.getcwd()
    data_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2]) +'\\[Data]'

    os.chdir(data_dir)

    # Assign path to local file(s)
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")

    # Print the result of the 'predictions' function
    predictions(turnstile_weather)


def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.

    This can be the same code as in the lesson #3 exercise.
    """

    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################

    Y = values
    X = features
    X = sm.add_constant(X)

    model = sm.OLS(Y, X)
    results = model.fit()

    output = results.params
    intercept = output[0]
    params = output[1:]

    ### If running locally, write the output of the .summary() method to an external file
    if __name__ == "__main__":
        with open('Regression Summary.txt', 'w') as f:
            f.write(str(results.summary()))

    return intercept, params



    fig, ax = plt.subplots(figsize=(8,6))

    ax.plot(x, y, 'o', label="data")
    ax.plot(x, y_true, 'b-', label="True")
    ax.plot(x, res.fittedvalues, 'r--.', label="OLS")
    ax.plot(x, iv_u, 'r--')
    ax.plot(x, iv_l, 'r--')
    ax.legend(loc='best');


def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.

    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe.
    We recommend that you don't use the EXITSn_hourly feature as an input to the
    linear model because we cannot use it as a predictor: we cannot use exits
    counts as a way to predict entry counts.

    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~10%) of the data contained in
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with
    this exercise on your own computer, locally. If you do, you may want to complete Exercise
    8 using gradient descent, or limit your number of features to 10 or so, since ordinary
    least squares can be very slow for a large number of features.

    If you receive a "server has encountered an error" message, that means you are
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features.
    '''
    ################################ MODIFY THIS SECTION #####################################
    # Select features. You should modify this section to try different features!             #
    # We've selected rain, precipi, Hour, meantempi, and UNIT (as a dummy) to start you off. #
    # See this page for more info about dummy variables:                                     #
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html          #
    ##########################################################################################

    # Convert days of the week into integers
    convert_to_weekdays = dataframe.DATEn.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    dataframe['day'] = convert_to_weekdays.apply(lambda x: datetime.strftime(x, '%w'))
    dataframe['day'] = dataframe['day'].astype(int) # convert data type to integer

    ### Using 'turnstile_data_master_with_weather.csv'
    features = dataframe[[]]

    dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
    dummy_hours = pd.get_dummies(dataframe['Hour'], prefix='hour')
    # dummy_date = pd.get_dummies(dataframe['DATEn'])
    dummy_weekdays = pd.get_dummies(dataframe['day'])

    features = features.join(dummy_units)
    features = features.join(dummy_hours)
    # features = features.join(dummy_date)
    features = features.join(dummy_weekdays)

    ### Preview features
    # print(features[0:10])

    # Values
    values = dataframe['ENTRIESn_hourly']

    # Perform linear regression
    intercept, params = linear_regression(features, values)

    predictions = intercept + np.dot(features, params)

    return predictions


### Call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()
