
import csv
from datetime import date

contacts = '9827688768'

filename = "contacts.csv"



def insert_contact(cont):
    input = cont +':'+ str(date.today())
    print(input)
    # rows = [cont +'-'+ date.today() , cont]
    rows = [input ,str(cont)]

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerow(rows)


def new_contact():
    print(contacts)
    with open(filename, newline='') as f:

        reader = csv.reader(f)
        for row in reader:

            contact = contacts

            if not row[-1] == contact or not row[-1] == "Phone":

                insert_contact(contact)
            else:
                print( "else",row , contact)














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

