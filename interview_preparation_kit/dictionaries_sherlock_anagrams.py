def sherlockAndAnagrams(s):
    new_list = s.split()
    print(new_list)
    directory = {x:y for x,y in zip(new_list[0],new_list[1])}
    for x,y in directory.items():
        if x != y:
            return 'NO'
    return "YES"