
s = '12:00:00AM'

def timeConversion(s):
    if s.endswith('AM') and int(s[0:2]) >= 12:
        return '0' + str(int(s[0:2]) - 12) + s[2:-2]
    elif s.endswith('AM') and int(s[0:2]) < 12:
        return s[0:-2]
    elif s.endswith('PM') and int(s[0:2]) < 10:
        return str(int(s[0:2]) + 12) + s[2:-2]
    elif s.endswith('PM') and int(s[0:2]) == 12:
        return s[0:-2]
    else:
        return str(int(s[0:2]) + 12) + s[2:-2]





print(timeConversion(s))