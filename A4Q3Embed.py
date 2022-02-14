from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")


db = client.A4dbEmbed
col = db.ArtistsTracks


a = col.aggregate([{"$unwind":"$ArtistsTracks"},
                   {"$unwind":"$ArtistsTracks.artist_ids"},
                   {"$group":{"_id":"$ArtistsTracks.artist_ids" ,"total_length":{"$sum":"$ArtistsTracks.duration"},
                              "artist_id":{"$first":"$ArtistsTracks.artist_ids"}}}])
for i in a:
    print(i)
