numToName = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    "4": "Four"
}
print(numToName["4"])
print(numToName[1])
print(numToName.get(5, "Invalid"))
print(numToName.get(3))
print(numToName.get(9, "Invalid"))