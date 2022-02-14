from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")


db = client.A4dbEmbed
col = db.ArtistsTracks

a = col.aggregate([{"$unwind":"$ArtistsTracks"},
                   {"$match":{"ArtistsTracks.track_id":{"$regex":"^70"}}},
                   {"$group":{"_id":'',
                              "avg_danceability":{"$avg":"$ArtistsTracks.danceability"}}}])

for i in a:
    print(i)
    print('\n')

