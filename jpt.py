def translate(sent):
    res = " "
    for letter in range(len(sent)):
        if sent[letter] in "AEIOUaeiou":
            res = res + "g"
        else:
            res = res + sent[letter]
    return res
def translateEasy(sent):
    res = " "
    for letter in sent:
        if letter in "AEIOUaeiou":
            res = res + "g"
        else:
            res = res + letter
    return res
print(translate(input("Enter Text: ")))
print(translateEasy(input("Enter Text: ")))