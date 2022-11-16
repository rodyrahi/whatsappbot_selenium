import csv
from datetime import date

contacts = ["y"]

filename = 'bot_V5/contacts.csv'


def insert_contact(cont):


    # rows = [cont +'-'+ date.today() , cont]
    rows = [str(cont).lower()]

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

            if cont in row:
                return True
            else:
                continue

        return False





