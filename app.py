# dict -> key, value
d = {
    "name" : "bold",
    "age" : 22
}
name1 = d["name"]
name2 = d.get("name")
d["friends"]="bat", "tulga"
d["ddd"]="aaa"
d["name"] = "tumur"
print(name1, name2)
print(d)