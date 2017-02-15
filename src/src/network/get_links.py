from network_construction import get_links

'''
This file separates the part of gettinnnng data from Twitter,
which is to avoid wasting time on requesting because the rate limit of Twitter
and overwriting existing files when testing the following algorithms
(network construction and community detection).
And it is also convenient for updating following algorithms.
'''

get_links('twitter', 'list_members_h_s')