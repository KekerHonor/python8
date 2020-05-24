person = {
    "name" : "bold",
    "age" : 22
}
for key in person:
    print(key)
for element in person.values():
    print(element)
for x,y in person.items():
    print(x,y)
# person.clear() buh elemeentuudiig ustgana
del person["age"]
print(person)