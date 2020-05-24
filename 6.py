person = [
    {
        "name":"bold",
        "age": 22,
        "friends":["delger","saraa"]
    },{
        "name":"tulga",
        "age": 25,
        "friends":["delger","bold","tuguldur"]
    },{
        "name":"bat",
        "age": 16,
        "friends":["purev"]
    }
]
zaluu = 0
ahmad = 0
for item in person:
    if item["age"] > ahmad:
        ahmad = item
print(ahmad)
