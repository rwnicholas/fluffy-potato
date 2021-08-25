#!/usr/bin/python3
import first
import follow

gramatica = {}
f = open("input3.txt", "r")

for x in f:
    a,b = x.split('->')
    b = b.rstrip('\n')
    gramatica[a] = b.split('|')


print(gramatica)
firstSet = first.run(gramatica.copy())
print("Conjunto First:", firstSet)
print("Conjunto Follow:", follow.run(firstSet, gramatica.copy()))