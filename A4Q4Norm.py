from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:27017/")

db = client.A4dbNorm
col1 = db.tracks_collection
col2 = db.artists_collection



a = col2.aggregate([{"$lookup":{"localField":"tracks",
                                "from": "tracks_collection",
                                "foreignField" : "track_id", "as": "T" }},
                    {"$unwind":"$T"},
                    {"$match":{"T.release_date":{"$gt":datetime.datetime(1950, 1, 1, 0, 0, 0, 0)}}},
                    {"$project":{"_id":1,
                              "name":1,
                              "t_name":"$T.name",
                              "t_release_date":"$T.release_date"}} ])
for i in a:
    print(i)