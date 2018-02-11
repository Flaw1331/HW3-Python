#PyBoss Script

#Importing essentials
import os
import csv

#Creating States abbreviations function
def state_abbrev(state):
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }

    #Changing the state to the abbreviation
    return(us_state_abbrev[state])

#Setting up  the file counts to interate through
file_count = ['1', '2']

#Iterating through each file
for flck in file_count:

    #Grabs the input file
    csvpath = os.path.join("raw_data", "employee_data" + flck + ".csv")

    #Creates output textfile
    output_path = os.path.join("raw_data", "employee_data_analyzed" + flck + ".csv")

    #Setting up variables
    empID = []
    first_name = []
    last_name = []
    DOB = []
    SSN = []
    state = []

    #Opening current file
    with open(csvpath, 'r', newline='') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        #Skipping headers
        next(csvreader, None)

        #Starting row reader for the file
        for row in csvreader:

            #Appending unchanged data
            empID.append(row[0])

            #Splitting the names into first and last names and appending to new variables
            f_name, l_name = row[1].split(" ")
            first_name.append(f_name)
            last_name.append(l_name)

            #Deconstructing the DOB and reordering it to liking
            year, month, day = row[2].split("-")
            DOB.append(str(month + "/" + day + "/" + year))

            #Readding in SSN and "encrypting" it so only the last numbers display
            first, second, third = row[3].split("-")
            SSN.append(str("***-**-" + third))

            #Appending the state abbreviation after calling the function to find it's abbrev
            state.append(state_abbrev(row[4]))

        #Creating cleaned zip in prep for output
        cleaned_csv = zip(empID,first_name,last_name,DOB,SSN,state)

        #Write to CSV File
        with open(output_path, 'w', newline='') as datafile:

            #initialize csv.writer
            csvwriter = csv.writer(datafile, delimiter =',')
            
            #Writing to CSV File
            csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
            csvwriter.writerows(cleaned_csv)            



