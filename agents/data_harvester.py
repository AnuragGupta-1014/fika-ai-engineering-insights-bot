# def harvest_data():
#     import json
#     with open("data/fake_events.json") as f:
#         return json.load(f)
# agents/data_harvester.py
def harvest_data():
    return [
        {
            "author": "Anurag",
            "additions": 120,
            "deletions": 60,
            "files_changed": 3
        },
        {
            "author": "Krishna",
            "additions": 90,
            "deletions": 40,
            "files_changed": 2
        }
    ]

