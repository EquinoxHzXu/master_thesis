import sys
sys.path.append("..")
from network.network_construction import *
import community
import matplotlib.pyplot as plt
import networkx as nx
from text_preprocessing import *
from text_mining import *
from pymongo import *
from to_csv import *
import numpy as np

def louvain_weighted(vectors, db, col):
    G = weighted_network_construction(vectors, db, col)

    partition = community.best_partition(G)
    pos = nx.spring_layout(G)
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
    labels = {}
    clusters = []

    for cluster in partition.values():
        clusters.append(cluster)

    for com in set(partition.values()):
        labels.clear()
        list_nodes = [nodes for nodes in partition.keys()
                      if partition[nodes] == com]
        for nodes in partition.keys():
            if partition[nodes] == com:
                labels[nodes] = nodes
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=500, node_color=colors[com], label=True)
        nx.draw_networkx_labels(G, pos, labels)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()

    return clusters


if __name__ == '__main__':
    client = MongoClient()
    db = client['twitter']
    col = db['list_members_h_s']

    texts, username = preprocessing_multiple_users('hs2', col.find())
    vectors, words = tf_idf(texts)

    clusters = louvain_weighted(vectors, 'twitter', 'links_h_s')
