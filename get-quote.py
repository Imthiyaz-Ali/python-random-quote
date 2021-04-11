import random
import requests


def primary():
    #print("Keep it logically awesome.")

    f = open("quotes.txt", 'a+')

    res = requests.get("https://animechan.vercel.app/api/random")
    res = res.json()
    newquote = res['quote']

    f.seek(0)
    fdata = f.readlines()
    # print(fdata)

    if fdata:
        f.write("\n")
#
    f.write(newquote)
    f.seek(0)
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    rnd = random.randint(0, last)

    print(quotes[rnd])


if __name__ == "__main__":
    primary()
