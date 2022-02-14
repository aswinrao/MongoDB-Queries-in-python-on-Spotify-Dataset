from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.A4dbEmbed
col = db.ArtistsTracks

a = col.aggregate([{"$unwind":"$tracks"},
                   {"$group":{"_id":"$_id","artist_id":{"$first":"$artist_id"},"name":{"$first":"$name"},"num_tracks":{"$count":{}}}},
                    {"$match":{"num_tracks":{"$gt":0}}}])

for i in a:
    print(i)
