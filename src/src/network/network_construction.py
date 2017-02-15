import sys
sys.path.append("..")
import time
import csv
from twitter_client import get_twitter_client
from to_csv import link_to_csv
from pymongo import *
from mongodb import *
import networkx as nx
from text.text_preprocessing import *
from text.text_mining import *
from sklearn.metrics.pairwise import *


def get_links(database, collection):
    api = get_twitter_client()
    client = MongoClient()
    db = client[database]
    col = db[collection]

    for user in col.find(no_cursor_timeout=True):
        current_user = api.get_user(user['_id'])
        friends = current_user.friends()
        for friend in friends:
            for existing_user in col.find():
                if friend.screen_name == existing_user['_id']:
                    print("Creating link between " + user['_id'] + " and " + friend.screen_name)
                    new_link = LinksHS(
                        user_screen_name=user['_id'],
                        user_id=user['id_str'],
                        friend_screen_name=friend.screen_name,
                        friend_id=friend.id_str
                    )
                    new_link.save()
        time.sleep(61)


def network_construction(database, collection):
    # get_links(database, collection)

    client = MongoClient()
    db = client[database]
    col = db[collection]

    link_to_csv('output/' + collection + '-original', 'twitter', 'links')
    G = nx.Graph()

    with open('output/' + collection + '-filtered' + '.csv', "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([
            'Source',
            'Target',
            'Type'
        ])
        for link in col.find(no_cursor_timeout=True):
            if (link['user_screen_name'] in G.nodes() and link['friend_screen_name'] in G.nodes()
                and (link['user_screen_name'], link['friend_screen_name'])in G.edges()):
                print("Link between " + link['user_screen_name']
                      + " and " + link['friend_screen_name'] + " has already existed.")
            else:
                G.add_node(link['user_screen_name'])
                G.add_node(link['friend_screen_name'])
                G.add_edge(link['user_screen_name'], link['friend_screen_name'])
                print("Edge between " + link['user_screen_name'] + " and "
                       + link['friend_screen_name'] + " has been added")
                csv_writer.writerow([
                    link['user_screen_name'],
                    link['friend_screen_name'],
                    'undirected'
                ])
    return G


def weighted_network_construction(vectors, database, collection):
    client = MongoClient()
    db = client[database]
    col = db[collection]

    link_to_csv('output/' + collection + '-original-weighted', 'twitter', 'links_h_s')
    G = nx.Graph()

    with open('output/' + collection + '-filtered-weighted' + '.csv', "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([
            'Source',
            'Target',
            'Type',
            'Weight'
        ])
        for link in col.find(no_cursor_timeout=True):
            if (link['user_screen_name'] in G.nodes() and link['friend_screen_name'] in G.nodes()
                and (link['user_screen_name'], link['friend_screen_name'])in G.edges()):
                print("Link between " + link['user_screen_name']
                      + " and " + link['friend_screen_name'] + " has already existed.")
            else:
                G.add_node(link['user_screen_name'])
                G.add_node(link['friend_screen_name'])
                G.add_edge(link['user_screen_name'], link['friend_screen_name'],
                           weight=get_weight(vectors, link['user_screen_name'], link['friend_screen_name']))
                print("Edge between " + link['user_screen_name'] + " and "
                       + link['friend_screen_name'] + " has been added")
                csv_writer.writerow([
                    link['user_screen_name'],
                    link['friend_screen_name'],
                    'undirected',
                    get_weight(vectors, link['user_screen_name'], link['friend_screen_name'])
                ])
    return G


def get_weight(vectors, user, friend):
    # Test case for the list 'HS'
    client = MongoClient()
    db = client['twitter']
    col = db['list_members_h_s']

    user_index = -1
    friend_index = -1

    for u in col.find():
        user_index += 1
        if u["_id"] == user:
            break

    for f in col.find():
        friend_index += 1
        if f["_id"] == friend:
            break

    cs = cosine_similarity(vectors[user_index], vectors[friend_index])

    return cs.item(0)
