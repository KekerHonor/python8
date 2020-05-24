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
nasandhursen = 0
for age in person:
    if age["age"]>=18:
        nasandhursen += 1
print("Nasand hursen hunii too:",nasandhursen)