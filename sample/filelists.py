#!/usr/bin/env python
# coding: UTF-8

import os

inpath = "."
outpath = "intglist.txt"

files = os.listdir(inpath)
txtlists = []

lists = []

for a in files:
    if a[-9:] == "_list.txt":
        txtlists.append(a)

#print txtlists

names = []
d = {}

for txtlist in txtlists:
    data = open(txtlist, "r")
    lines = data.readlines()

    for line in lines:
        if line[-6:] == ".pdf\r\n":
            #lists.append(line)
            d.setdefault(line, 0)

            if line in d:
                d[line] = d[line] + 1

    data.close()

output = open(outpath, "w")

key = d.keys()
value = d.values()
s = 0

for i in range(len(d)):
    output.write(str(key[i][:-2]) + ',' + str(value[i]) + '\r\n')
    s += value[i]

output.write("num = " + str(len(d)) + '\r\n')
output.write("sum = " + str(s))

output.close()
