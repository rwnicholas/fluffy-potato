from first import hasVoid, flattenArray, concatDicts

follow = {}

def getFirst(gramatica, firstSet, beta):
    if len(beta) >= 1:
        # Regra 0, 1 e 2 do First
        if beta[0] == 'ε':
            return beta[0]
        elif beta[0].islower():
            return beta[0]
        
        # Caso seja não-terminal, o valor já foi calculado
        if len(beta) == 1:
            return firstSet[beta[0]]
        
        if hasVoidInBeta(beta, gramatica):
            return flattenArray(firstSet[beta[0]] + list(getFirst(firstSet, beta[1:])))
        return firstSet[beta[0]]

def getIndex(elemento, lista):
    indexes = {}
    for producaoI, producao in enumerate(lista):
        if elemento in producao:
            indexes[producaoI] = [i for i, e in enumerate(producao) if e == elemento]
            indexes[producaoI] = indexes[producaoI][0]
    return indexes

def hasVoidInBeta(beta, gramatica):
    for i in beta:
        if i.islower():
            return False
        if hasVoid(i, gramatica):
            return True
        return False

def followSet(firstSet, gramatica):
    head = next(iter(gramatica))
    if not head in follow.keys():
        follow[head] = ['$']

    # É necessário inicializar as chaves
    for a in gramatica.keys():
        if not a in follow.keys():
            follow[a] = []

    for a in gramatica.keys():
        for s,b in gramatica.items():
            indexes = getIndex(a,b)
            if indexes:
                for x,y in indexes.items():
                    beta = b[x][(y+1):]
                    if len(b[x]) > y+1:
                        if len(beta) >= 1:
                            firstFromBeta = getFirst(gramatica, firstSet, beta)
                            firstFromBeta = flattenArray(firstFromBeta)
                            follow[a].append(firstFromBeta)
                            follow[a] = flattenArray(follow[a])
                            if 'ε' in follow[a]:
                                follow[a].remove('ε')
                    if hasVoidInBeta(beta, gramatica) or not beta:
                        follow[s] = flattenArray(follow[s])
                        follow[a].append(follow[s])
                        follow[a] = flattenArray(follow[a])
    
    return follow


def run(firstSet, gramatica):
    for i in range(2):
        followSet(firstSet, gramatica)

    for a,b in follow.items():
        follow[a] = flattenArray(b)
    
    return follow