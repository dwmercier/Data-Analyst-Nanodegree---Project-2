import numpy as np
import scipy


def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.

    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''

    # Set up counter and empty lists for residuals and deviations
    counter = 0
    residuals = []
    deviations = []

    # Calculate the mean of the data
    data_mean = np.mean(data)

    # Loop through data and add each individual squared residual and deviation to their respective lists
    for y in data:
        residual = data[counter] - predictions[counter]
        deviation = data[counter] - data_mean
        residuals.append(residual**2)
        deviations.append(deviation**2)
        counter += 1

    # Sum up residuals and deviations
    residuals_sum = np.sum(residuals)
    deviations_sum = np.sum(deviations)

    # Compute r squared
    r_squared = 1 - (residuals_sum/deviations_sum)

    return r_squared

