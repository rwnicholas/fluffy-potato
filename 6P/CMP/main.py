#!/usr/bin/python3
import first

gramatica = {}
f = open("input3.txt", "r")

for x in f:
    a,b = x.split('->')
    b = b.rstrip('\n')
    gramatica[a] = b.split('|')

print(first.run(gramatica.copy()))