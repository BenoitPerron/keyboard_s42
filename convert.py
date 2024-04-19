import json

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

corne = json.load(open("miryoku-configurator-crkbd.json", "r"))
# print(corne)

out={    "version": 1,
    "uid": 4882409417170782975,
    "layout": []}

for l in corne["layers"]:
    newlayer = list(split(l, 6))

    out["layout"].append(newlayer)

fout = open("fout.vil", "w")
json.dump(out, fout)
fout.close()
