def joinList(list):
    listSize = len(list)
    #replace last item with and

    list[listSize-1] = 'and ' + list[listSize-1]
    joinedStr = ", ".join(list)
    return joinedStr


sampleList = ['apples', 'bananas', 'tofu', 'cats']
joinedListStr = joinList(sampleList)

print (joinedListStr)