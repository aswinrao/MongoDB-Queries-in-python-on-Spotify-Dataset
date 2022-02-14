from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")


db = client.A4dbNorm
col = db.tracks_collection

a = col.aggregate([{"$unwind":"$artist_ids"},
                   {"$group":{"_id":"$artist_ids" ,"total_length":{"$sum":"$duration"},
                              "artist_id":{"$first":"$artist_ids"}}},
                   {"$match":{"total_length":{"$gt":0}}}])
for i in a:
    print(i)
