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
dundaj = 0
nasandhursen = 0
for age in person:
    dundaj += age["age"]
print(dundaj/3)