
import csv
from datetime import date

contacts = ["", "y"]

filename = "contacts.csv"



def insert_contact(cont):
    input = cont +':'+ str(date.today())
    print(input)
    # rows = [cont +'-'+ date.today() , cont]
    rows = [str(cont)]

    # writing to csv file
    with open(filename, 'a',newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerow(rows)


def new_contact(cont):

    with open(filename, 'r',newline='') as f:

        reader = csv.reader(f)
        for row in reader:



            if cont == row:
                print(row)
                return False
            else:
                return True














# # field names
# fields = ['Contact']
#
# # data rows of csv file
# rows = [['Nikhil']]
#
# # name of csv file
#
#
# # writing to csv file
# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
#
#     # writing the fields
#     csvwriter.writerow(fields)
#
#     # writing the data rows
#     csvwriter.writerows(rows)

