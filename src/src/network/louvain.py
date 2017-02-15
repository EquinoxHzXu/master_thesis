import sys
sys.path.append("..")
from network_construction import *
import community
import matplotlib.pyplot as plt
import networkx as nx
from text.text_preprocessing import *
from text.text_mining import *
from pymongo import *


def louvain_unweighted(db, col):
    G = network_construction(db, col)

    partition = community.best_partition(G)
    pos = nx.spring_layout(G)
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
    labels = {}

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


def louvain_weighted(db, col):
    G = weighted_network_construction(db, col)

    partition = community.best_partition(G)
    pos = nx.spring_layout(G)
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
    labels = {}

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


if __name__ == '__main__':
    client = MongoClient()
    db = client['twitter']
    col = db['list_members_h_s']

    texts, username = preprocessing_multiple_users('hs', col.find())
    vectors, words = tf_idf(texts)

    louvain_weighted('twitter', 'list_members_h_s')


