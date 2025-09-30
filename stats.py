def wordCount(book=None):
    words = book.split()
    return len(words)


def charCounter(book=None):
    charDict = {}
    for char in book:
        char = char.lower()
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    return charDict


def sortedList(charDict):
    newList = []
    for key, value in charDict.items():
        tempDict = {}
        if key.isalpha():
            tempDict["char"] = key
            tempDict["num"] = value
            newList.append(tempDict)
    return sorted(newList, key=lambda x: x["num"], reverse=True)
