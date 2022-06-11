import json
import requests
listy = ["0061186422", "0131103628", "0596002254", "0000000000", "0486291464", "1593275994", "1502632950", "1138763683", "0898711878", "0080535925", "0198250797", "082182676X", "3662607697", "0252725484", "0062515861", "0000000000",
         "0061186422", "0131103628", "0596002254", "0000000000", "0486291464", "1593275994", "1502632950", "1138763683", "0898711878", "0080535925", "0198250797", "082182676X", "3662607697", "0252725484", "0062515861", "0000000000"]
chiperKey = ["1", "5", "22", "{", "1", "36", "6",
             "8", "24", "15", "17", "13", "16", "40", "7", "}"]
titles = []


def getTitle(t):
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'.format(t))
    r = r.text
    rr = json.loads(r)
    try:
        keyz = rr["items"][0]
        return keyz["volumeInfo"]["title"]
    except:
        pass


def getFlag():
    flag = ""
    count = 0
    for i in titles:
        try:
            flag = flag + (i[int(chiperKey[count])-1])
            count += 1
        except:
            try:
                flag = flag + chiperKey[count]
                count += 1
            except:
                pass
    return flag


for i in listy:
    titles.append(getTitle(i))

print(getFlag())
