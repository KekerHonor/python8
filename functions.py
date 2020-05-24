def car_count(data: list, name: "str")->int:
    for item in data:
        if item["ner"] == name:
            return len(item["mashinuud"])
def friends(data: list, name: "str"):
    for item in data:
        if item["ner"] == name:
            print("Naizud: ",item["naizuud"])
def age(data: list, name: "str"):
    for item in data:
        if item["ner"] == name:
            print("Nas: ",item["nas"])