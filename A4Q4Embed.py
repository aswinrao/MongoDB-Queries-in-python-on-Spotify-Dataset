from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:27017/")

db = client.A4dbEmbed
col = db.ArtistsTracks

a = col.aggregate([{"$unwind": "$ArtistsTracks"},
                   {"$match": {"ArtistsTracks.release_date": {"$gte": datetime.datetime(1950, 1, 1, 0, 0, 0, 0)}}},
                   {"$unset": ["artist_id", "followers", "popularity", "genres", "tracks"]},
                   {"$project": {"_id": 1,
                                 "name": 1,
                                 "t_name": "$ArtistsTracks.name",
                                 "t_release_date": "$ArtistsTracks.release_date"}}])


for i in a:
    print(i)
