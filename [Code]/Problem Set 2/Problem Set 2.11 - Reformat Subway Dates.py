import datetime


### Assign local environment variables and call function(s) if necessary
def main():
    # Assign test date to local variable
    date = '12-30-72'

    # Print the output of the 'reformat_subway_dates' function 
    print(reformat_subway_dates(date))


def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There are a couple of useful functions in the datetime library that will
    help on this assignment, called strptime and strftime. 
    More info can be seen here and further in the documentation section:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''

    date_formatted = datetime.datetime.strptime(date, '%m-%d-%y').strftime("%Y-%m-%d") # your code here

    return date_formatted


### Call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()
