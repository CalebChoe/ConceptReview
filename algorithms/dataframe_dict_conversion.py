import pandas as pd

name = ["player1", "player2", "player3", "player4"]
monsters_killed = [['zombie', 'zombie'], ['zombie', 'zombie', 'zombie'], ['zombie'], ['zombie', 'zombie', 'zombie', 'zombie']]

dictionary = {'name': name, 'monsters_killed': monsters_killed}

df = pd.DataFrame(dictionary)

print(df)

d = dict()

namelen = len(name)
if namelen == len(monsters_killed):
    for i in range(namelen):
        d[name[i]] = monsters_killed[i]
else:
    print("value counts do not match")

print(d)
