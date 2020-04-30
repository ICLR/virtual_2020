import csv
import yaml
d = []
cur = "Diamond"
li = []
for i, l in enumerate(csv.reader(open("sponsors.tsv"), delimiter="\t")):
    if i == 0:
        continue

    if l[1] != cur:
        d.append({"tier":cur, "vals":li})
        cur = l[1]
        li = []
    li.append({"name": l[0], "img": l[2]})
print(yaml.dump({"sponsors": d}))
