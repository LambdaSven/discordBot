import random
import requests
import json

def make_lichess_link():
    url = "https://lichess.org/api/challenge/open"
    params = {'clock.limit': 180*60, 'clock.increment': 60,'variant': 'standard'}
    resp = requests.post(url, params)
    print("Making Reqest to Lichess in make_lichess_link")
    return resp.json()["challenge"]["url"]

def find_part(s: str):
    url = "https://mhw-db.com/monsters"
    resp = requests.get(url)
    print("Making Request to mhw-db in find_part")
    j = resp.json()
    ret = "This drop is found in..."
    for x in j:
        if len(x["rewards"]) > 0:
            for e in x["rewards"]:
                if e["item"]["name"].lower() == s.lower():
                    ret += "\n\t" + x["name"]
    return ret

def print_monster(s: str):
    m = return_monster(s)
    name = m["name"]
    elements = m["elements"]
    ailments = m["ailments"]
    weaknesses = m["weaknesses"]
    drops = m["rewards"]
    output = ""
    output += "**" + name + "**\n"
    output += "Deals: \n"
    for x in elements:
        output += "\t " + x + "\n"    
    output += "Causes: \n"
    for x in ailments:
        output += "\t " + x["name"] + "\n"
    output += "\n Is weak to:\n"
    for x in weaknesses:
        output += "\t " + x["element"] + " " + str(x["stars"]) + "\n"
    output += "\n Drops: \n"
    for x in drops:
        output += "\t " + x["item"]["name"] + "\n"
    return output 

def return_monster(s: str):
    url = "https://mhw-db.com/monsters"
    print("Making request to mhw-db in return_monster")
    resp = requests.get(url)
    j = resp.json()
    for x in j:
        if x["name"].lower() == s.lower():
            return x

def make_user_dict():
    f = open("data/users.txt",'r').readlines()
    d = {}
    for x in f:
        s = x.split(',')
        d[int(s[0])] = str(s[1]).strip()
    return d

def generate_name():
    F = open("data/firstnames.txt", "r")
    f = F.readlines()
    F.close()
    L = open("data/lastnames.txt", "r")
    l = L.readlines()
    L.close()

    return f[random.randrange(0, len(f))].strip() + " " + l[random.randrange(0, len(l))].strip()

def addfirst(s):
    f = open("data/firstnames.txt", "a")
    f.write(s + "\n")
    f.close()

def addlast(s):
    f = open("data/lastnames.txt", "a")
    f.write(s + "\n")
    f.close()

def addWords(s):
    f = open("data/saidWords.txt", "a")
    f.write(s + "\n")
    f.close()

