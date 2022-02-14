
from bson.json_util import loads
from pymongo import MongoClient


# Use client = MongoClient('mongodb://localhost:27017') for specific ports!
# Connect to the default port on localhost for the mongodb server.
client = MongoClient("mongodb://localhost:27017/")


# Create or open the A4DBNorm database on server.
db = client["A4dbEmbed"]
print(client.list_database_names())


# Create or open the collection in the db
artists_collection = db["artists_collection"]
artists_collection.insert_one({"a":1})


tracks_collection = db["tracks_collection"]
tracks_collection.insert_one({"a":1})


artists_collection.delete_many({})
tracks_collection.delete_many({})

with open ('artists.json' ) as f:
    data = loads(f.read())
artists_collection.insert_many(data)


with open('tracks.json','rb') as t:
    data1 = loads(t.read())
tracks_collection.insert_many(data1)

ArtistsTracks = db["ArtistsTracks"]
ArtistsTracks.insert_one({"a":1})
ArtistsTracks.delete_many({})


a=db.artists_collection.aggregate([{
    "$lookup":{
        "localField": "tracks",
        "from" : "tracks_collection",
        "foreignField": "track_id",
        "as": "ArtistsTracks"
    } 
}])


ArtistsTracks.insert_many(a)

artists_collection.drop()
tracks_collection.drop()

client.close()