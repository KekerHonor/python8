import new
p = new.person
a = 0
for item in p:
    if len(item["friends"]) > a:
        a = len(item["friends"])
        index = person.index(item)
print(person[index])