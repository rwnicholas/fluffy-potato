#!/usr/bin/python3
import first
import follow
import csv

def exportDictToCSV(dict1, filename):
    a_file = open(filename+".csv", "w")
    writer = csv.writer(a_file)
    for key, value in dict1.items():
        writer.writerow([key, value])

    a_file.close()

gramatica = {}
f = open("input2.txt", "r")

for x in f:
    a,b = x.split('->')
    b = b.rstrip('\n')
    gramatica[a] = b.split('|')


firstSet = first.run(gramatica.copy())
followSet = follow.run(firstSet, gramatica.copy())
print("Conjunto First:", firstSet)
print("Conjunto Follow:", followSet)
# exportDictToCSV(firstSet, "item2_conjunto_first")
# exportDictToCSV(followSet, "item2_conjunto_follow")