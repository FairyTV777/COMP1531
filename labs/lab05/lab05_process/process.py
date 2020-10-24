import pickle
from collections import Counter
import json

def process():
    pickleFile = open("shapecolour.p", "rb")
    pairs = pickle.load(pickleFile)
    pairsTuple = [(pair['colour'], pair['shape']) for pair in pairs]
    frequency = Counter(pairsTuple)
    mostTuple = max(pairsTuple, key=frequency.get)
    bigger = {}
    bigger['mostCommon'] = {'colour': mostTuple[0], 'shape': mostTuple[1]}
    bigger['rawDate'] = pairs
    with open('processed.json', 'w') as FILE:
        json.dump(bigger, FILE)

if __name__ == '__main__':
    process()