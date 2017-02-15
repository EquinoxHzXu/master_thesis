from mongoengine import *

connect("twitter")


class ListMembers(Document):
    screen_name = StringField(primary_key=True)
    id_str = StringField(required=True)
    friends_count = IntField(required=True)


class Links(Document):
    user_screen_name = StringField()
    user_id = StringField()
    friend_screen_name = StringField()
    friend_id = StringField()


class ListMembersRV(Document):
    screen_name = StringField(primary_key=True)
    id_str = StringField(required=True)
    friends_count = IntField(required=True)


class LinksRV(Document):
    user_screen_name = StringField()
    user_id = StringField()
    friend_screen_name = StringField()
    friend_id = StringField()


class ListMembersHS(Document):
    screen_name = StringField(primary_key=True)
    id_str = StringField(required=True)
    friends_count = IntField(required=True)


class LinksHS(Document):
    user_screen_name = StringField()
    user_id = StringField()
    friend_screen_name = StringField()
    friend_id = StringField()
