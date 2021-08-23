def repeatedString(n, string):
    list_letter = [x for x in string]
    counter = 0
    for x in range(n-1):
        first = list_letter[x]
        list_letter.insert(-1, first)
    for x in list_letter:
        if x == 'a':
            counter +=1


    return counter