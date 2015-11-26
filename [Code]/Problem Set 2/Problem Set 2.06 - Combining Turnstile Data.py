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

    # Assign local output file path
    output_file = "updated_turnstile_110528.txt"

    # Run the 'create_master_turnstile_file' function to read and write using local files
    create_master_turnstile_file(filenames, output_file)


def create_master_turnstile_file(filenames, output_file):
    '''
    Write a function that takes the files in the list filenames, which all have the 
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file. The input files do not have column header
    rows of their own.
    
    For example, if file_1 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    
    and another file, file_2 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 3 ...
    line 4 ...
    line 5 ...
    
    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''

    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        master_file = csv.writer(master_file)
        
        for name in filenames:
            # your code here
            with open(name, 'r') as input_file:
                reader = csv.reader(input_file)

                for row in reader:
                    master_file.writerow(row)


### Call the 'main' function to setup the local environment
if __name__ == "__main__":
    main()
