import csv


### Assign local environment variables and call function(s) if necessary
def main():

    # Set local directory for data files
    import os

    current_dir = os.getcwd()
    data_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2]) +'\\[Data]\\turnstile_txt'

    os.chdir(data_dir)

    # Read all text files in directory into list
    filenames = os.listdir(data_dir)
    
    # Remove updated files from file list to avoid processing them with fix_turnstile_data
    def filter_files(filenames):
        for f in filenames:
            if 'updated' in f:
                filenames.remove(f)

    filter_files(filenames)

    # Run the 'fix_turnstile_data' function to read and write using local files
    fix_turnstile_data(filenames)


def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
   
    for name in filenames:
        # Setup input and output files
        f_in = open(name, 'r')
        f_out = open('updated_' + name, 'w') 
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        # Store the header values from the first row
        for row in reader:
            row_header = row[0:3]
            row_body = row[3:len(row)]
            formatted_row = ""
            row_pos = 0
            
            #Iterate over all the rows in the list and append the header items to each
            while row_pos < len(row_body):
                formatted_row = row_header + row_body[0 + row_pos:5 + row_pos]
                row_pos += 5
                writer.writerow(formatted_row)
        

### Call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()
