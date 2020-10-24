from collections import Counter
import pickle

def most_common():
    pickleFile = open("shapecolour.p", 'rb')
    pairs = pickle.load(pickleFile)
    pairsTuple = [(pair['colour'], pair['shape']) for pair in pairs]
    frequency = Counter(pairsTuple)
    mostTuple = max(pairsTuple, key=frequency.get)
    most = {}
    most['colour'] = mostTuple[0]
    most['shape'] = mostTuple[1]
    pickleFile.close()
    return most
