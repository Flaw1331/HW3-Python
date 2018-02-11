#PyBank Script

#Importing essentials
import os
import csv

#Setting up  the file counts to interate through
file_count = ['1', '2']

#Iterating through each file
for flck in file_count:

    #Grabs the input file
    csvpath = os.path.join("raw_data", 'budget_data_' + flck + '.csv')

    #Creates output textfile
    output_path = os.path.join("raw_data", 'budget_data_analyzed_' + flck + '.txt')

    #Setting up variables
    date = []
    revenue = []
    rev_sum = 0
    inc_gr = 0
    dec_gr = 0
    counter = 0

    #Opening current file
    with open(csvpath, 'r', newline='') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        #Skipping headers
        next(csvreader, None)

        #Starting row reader for the file
        for row in csvreader:

            #Appending each row to it's list
            date.append(row[0])
            revenue.append(int(row[1]))

            #Collecting sum of revenue
            rev_sum += int(row[1])

            #Checking to make sure there is enough data to calculate a change
            if len(date) > 1:

                #Checking if revenue increased or decreased and if it's the greatest recorded
                if revenue[counter] < revenue[counter-1]:
                    if (revenue[counter-1] - revenue[counter]) > dec_gr:
                        dec_gr = revenue[counter-1] - revenue[counter]
                        dec_date = date[counter]
                elif revenue[counter] > revenue[counter-1]:
                    if (revenue[counter] - revenue[counter-1]) > inc_gr:
                        inc_gr = revenue[counter] - revenue[counter-1]
                        inc_date = date[counter]
                else:
                    pass
            
            #Incriment counter
            counter += 1

        #Print results
        print("Financial Analysis for budget_data_" + flck)
        print("--------------------------------------------")
        print("Total Months: " + str(len(date)))
        print("Total Revenue: $" + str(rev_sum))
        print("Average Revenue Change: $" + str(round(rev_sum/len(date),2)))
        print("Greatest Increase in Revenue: " + inc_date + " ($" + str(inc_gr) + ")")
        print("Greatest Decrease in Revenue: " + dec_date + " ($-" + str(dec_gr) + ")")
        print("")
    
        #Write to TXT File
        with open(output_path, 'w') as txtfile:

            #Writing output
            txtfile.write("Financial Analysis for budget_data_" + flck + "\n")
            txtfile.write("--------------------------------------------" + "\n")
            txtfile.write("Total Months: " + str(len(date)) + "\n")
            txtfile.write("Total Revenue: $" + str(rev_sum) + "\n")
            txtfile.write("Average Revenue Change: $" + str(round(rev_sum/len(date),2)) + "\n")
            txtfile.write("Greatest Increase in Revenue: " + inc_date + " ($" + str(inc_gr) + ")" + "\n")
            txtfile.write("Greatest Decrease in Revenue: " + dec_date + " ($-" + str(dec_gr) + ")" + "\n")