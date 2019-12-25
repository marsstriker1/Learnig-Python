print("Basic String Output.\nNext line\tTab\t\'Quotation\'\t \"This too\".")
str1 = "Stored string"
print("Printing " + str1 + " using concatenation.")
print(str1.lower() + " " + str1.upper())
print(str1.isupper())
print(str1.upper().isupper())
print(len(str1))
print(str1[0] + " " + str1[12])
print(str1.index(" "))
print(str1.index("stri"))
#print(str1.index("gfs")) this gives an error as gfs is not in str1
print(str1.replace("Stored","Test"))

