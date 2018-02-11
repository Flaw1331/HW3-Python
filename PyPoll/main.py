#PyPoll Script

#Importing essentials
import os
import csv

#Setting up  the file counts to interate through
file_count = ['1', '2']

#Iterating through each file
for flck in file_count:

    #Grabs the input file
    csvpath = os.path.join("raw_data", "election_data_" + flck + ".csv")

    #Creates output textfile
    output_path = os.path.join("raw_data", "election_data_analyzed_" + flck + ".csv")

    #Setting up variables
    total_votes = 0
    candidates = {}

    #Opening current file
    with open(csvpath, 'r', newline='') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        #Skipping headers
        next(csvreader, None)

        #Starting row reader for the file
        for row in csvreader:

            #Appending unchanged data
            if row[2] in candidates:
                candidates[str(row[2])] += 1
            else:
                candidates[str(row[2])] = 1

            #Finding total votes
            total_votes += 1




        #Printing results
        print("Election Results")
        print("-------------------")
        print("Total Votes: " + str(total_votes))
        print("-------------------")
        for names in candidates:
            print(str(names) + ": " + str(round((candidates[names]/total_votes),3) * 100) + "% (" + str(candidates[names]) + ")")
        print("-------------------")
        print("Winner: " + str(max(candidates,key=candidates.get)))
        print("-------------------")



        #Write to TXT File
        with open(output_path, 'w') as txtfile:

            #Writing output
            txtfile.write("Election Results" + "\n")
            txtfile.write("-------------------" + "\n")
            txtfile.write("Total Votes: " + str(total_votes) + "\n")
            txtfile.write("-------------------" + "\n")
            for names in candidates:
                txtfile.write(str(names) + ": " + str(round((candidates[names]/total_votes),3) * 100) + "% (" + str(candidates[names]) + ")" + "\n")
            txtfile.write("-------------------" + "\n")
            txtfile.write("Winner: " + str(max(candidates,key=candidates.get)) + "\n")
            txtfile.write("-------------------" + "\n")