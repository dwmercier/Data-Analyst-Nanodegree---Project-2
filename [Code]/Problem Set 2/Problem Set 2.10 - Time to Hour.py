import pandas


### Assign local environment variables and call function(s) if necessary
def main():
    
    # Assign test times to list
    times = ['00:30:00', '01:30:00', '21:30:00']

    # Print the output of the 'time_to_hour' function using test times in list
    for t in times:
        print(time_to_hour(t))


def time_to_hour(time):
    '''
    Given an input variable time that represents time in the format of:
    "00:00:00" (hour:minutes:seconds)
    
    Write a function to extract the hour part from the input variable time
    and return it as an integer. For example:
        1) if hour is 00, your code should return 0
        2) if hour is 01, your code should return 1
        3) if hour is 21, your code should return 21
        
    Please return hour as an integer.
    '''
    
    hour = int(time[0:2]) / 1  # your code here

    return int(hour)


### Call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()