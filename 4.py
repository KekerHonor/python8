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
d1 = 0
c1 = 0
d2 = 0
c2 = 0
for age in person:
    if age["age"] >= 18:
        d1 += age["age"]
        c1+=1
    else:
        d2+=age["age"]
        c2+=1
print(abs(d1/c1-d2/c2))
