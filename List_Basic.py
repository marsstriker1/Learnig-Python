#[ ] are used to define lists
colours = [ "Red", "Blue", "Green"]
print(colours)
print(colours[1])
print(colours[-1]) #-ve access items from the back e.g. -1,-2,-3...
colours = [ "Red", "Blue", "Green", "Yellow", "Orange", "Black"]
print(colours[1:])
print(colours[1:3])
print(colours[1])
colours[1] = "Navy Blue"
print(colours[1])
num_colours = [ "Red",2 , "Green", 4, "Orange", "Black"] #Lists can have mixed data types
print(num_colours[1:])
print(num_colours[1:3])
colours.extend(num_colours)
print(colours)
num_colours.append(7) #adds a list to another
print(num_colours)
num_colours.insert(0, "Grey") #inserts an element at certain index and the shifts all other existing items
print(num_colours)
num_colours.remove("Grey") #removes certain elements
print(num_colours)
num_colours.pop()   #removes last element
print(num_colours)
print(num_colours.index("Orange"))      #Searches and returns the index of given item
num_colours.insert(5,"Green")
print(num_colours.count("Green"))
names=["Ravi", "Sumit", "Mark"]
names2 = names.copy()
names.sort()
print(names)
nos=[1, 5, 3, 4, 2]
nos.sort()
print(nos)
print("Unsorted list = ", names2)       #cannot concatenate strings and lists using '+'
print("Sorted list = ", names)

