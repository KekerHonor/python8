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
a = 0
for item in person:
    if len(item["friends"]) > a:
        a = len(item["friends"])
        index = person.index(item)
print(person[index])