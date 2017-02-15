import csv
from pymongo import MongoClient

client = MongoClient()

def link_to_csv(filename, database, collection):
    db = client[database]
    col = db[collection]
    with open(filename + '.csv', "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([
            'User Screen Name',
            'Friend Screen Name'
        ])
        for user in col.find():
            csv_writer.writerow([
                user['user_screen_name'],
                user['friend_screen_name']
            ])
            print("Link between " + user['user_screen_name'] + " and "
               + user['friend_screen_name'] + " has been written.")
