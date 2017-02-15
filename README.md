# DECO7861-THESIS
A github repository for Master thesis of the University of Queensland

## What is included
1. Louvain Algorithm
2. Text clustering by TF-IDF and agglomerative clustering
3. Louvain Algorithm on a weighted graph, where the weights are the cosine similarities of TF-IDF

## How to use
1. Create your app on Twitter and get your tokens, then fill in the variables in twitter_client.py
2. Install MongoDB, open the terminal, run "mongod" to start the MongoDB server

### Louvain Algorithm
1. Run network/get_list_members.py to collect the informaiton of users (users must be in a list)
2. Run network/get_links.py to get the relationship of users
3. Run the function louvain_unweighted() in network/Louvain.py
4. A csv file for the network is generated and it can be used in Gephi

### Text clustering
1. Run text/get_timeline.py to collect Tweets
2. Run text/text_mining.py

### Louvain Algorithm on a weighted graph
1. Run network/get_list_members.py collect the informaiton of users
2. Run text/get_timeline.py to collect Tweets
3. Run the function louvain_weighted() in network/Louvain.py
4. A csv file for the network is generated and it can be used in Gephi

## Notice
There are several names of lists and the name of MongoDB collections and if you want to apply to your cases you need to change them.
