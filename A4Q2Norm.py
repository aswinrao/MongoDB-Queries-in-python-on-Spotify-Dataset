import pymongo

#from A4T2 import ArtistsTracks
# Use client = MongoClient('mongodb://localhost:27017') for specific ports!
# Connect to the default port on localhost for the mongodb server.
client = pymongo.MongoClient("mongodb://localhost:27017")

# Open the A4 Norm database on server.
db = client.A4dbNorm
tracks_collection = db.tracks_collection

q2 = tracks_collection.aggregate([
    {
        "$match":{  "track_id": { "$regex": "^70" } }
    },
    {
        "$group" :{
            "_id":"",
            "'avg_danceability'" : { "$avg": "$danceability" }
        }
    }
])

for i in q2:
    print(i)
