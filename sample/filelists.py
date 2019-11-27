#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

inpath = "."
outpath = "intglist.txt"

files = os.listdir(inpath)

#input .txt
txtlists = []

for a in files:
    if a[-9:] == "_list.txt":
        txtlists.append(a)

d = {}

for txtlist in txtlists:
    data = open(txtlist, "r")
    lines = data.readlines()

    #read .pdf in .txt
    for line in lines:
        if line[-6:] == ".pdf\r\n":
            d.setdefault(line, 0)

            if line in d:
                d[line] = d[line] + 1

    data.close()

#make integrated lists
key = d.keys()
value = d.values()
count = 0

lists = []

for i in range(len(d)):
    lists.append(str(key[i][:-2]) + ',' + str(value[i]) + '\r\n')
    count += value[i]

lists.sort()

#output intglist.txt
output = open(outpath, "w")

for l in lists:
    output.write(l)

#number of lists and sum of lists
output.write("num = " + str(len(d)) + '\r\n')
output.write("sum = " + str(count))

output.close()
