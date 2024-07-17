d = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(d)
print(d["brand"])
print(d["year"])
print(len(d))
print(type(d))

nd = dict.copy(d)
nd["newkey"] = 1234
print(nd)
nd.clear()
print(nd)
