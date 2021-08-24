#!/usr/bin/python3
import numpy as np

first = {}

def hasVoid(B, first):
    if B in first.keys():
        if 'ε' in first[B]:
            return True
    return False

def concatDicts(test_dict1, test_dict2):
    for key in test_dict1: 
        if key in test_dict2: 
            for val in test_dict1[key]:
                if val not in test_dict2[key]:  
                    test_dict2[key].append(val)
        else: 
            test_dict2[key] = test_dict1[key][:]
    
    return test_dict2

def flattenArray(array):
    tmp = np.hstack(array).squeeze()
    return list(set(tmp)).copy()

def firstSet(linha):
    global first

    # Regra 0, 1 e 2 do First
    for a,b in reversed(linha.items()):
        if not a in first.keys():
            first[a] = []

        for i in b:
                if i == 'ε':
                    first[a].append(i)
                elif i[0].islower():
                    first[a].append(i[0])

    # Regra 3 do First
    for a,b in reversed(linha.items()):
        for i in b:
            if i[0].isupper():
                if len(i) > 1:
                    if not hasVoid(i[0], first):
                        first[a].append(first[i[0]])
                        first[a] = flattenArray(first[a])
                    else:
                        B = first[i[0]].copy()
                        B.remove('ε')
                        first[a].append(B)
                        first[a] = flattenArray(first[a])
                        alpha = i[1:]
                        tmpfirst = concatDicts(first, firstSet({a: alpha}))
                        first = tmpfirst.copy()
                elif len(i) == 1:
                    first[a].append(first[i])
                    first[a] = flattenArray(first[a])


    return first

def run(arg):
    linhas = arg
    # For duas vezes para garantir que os campos foram preenchidos corretamente,
    # mesmo que um não-terminal tenha mudado 
    for i in range(2):
        firstSet(linhas)
    
    for a,b in first.items():
        first[a] = flattenArray(b)

    return first