import gensim
import pickle
import csv
import sys
import gzip
import logging
import numpy
from numpy import linalg
from scipy.spatial import distance
from gensim.models import KeyedVectors

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def headToHead(word1,word2):
    newVec = []
    for i in range(0,len(word1)):
        newVec.append(word2[i]-word1[i])
    return newVec


nostop = True
inFile = sys.argv[1]
if nostop:
    word_vectors_25 = KeyedVectors.load("vecs_25_nostop.kv", mmap='r')
    word_vectors_35 = KeyedVectors.load("vecs_35_nostop.kv", mmap='r')
    word_vectors_45 = KeyedVectors.load("vecs_45_nostop.kv", mmap='r')
    word_vectors_55 = KeyedVectors.load("vecs_55_nostop.kv", mmap='r')
    word_vectors_65 = KeyedVectors.load("vecs_65_nostop.kv", mmap='r')
    word_vectors_75 = KeyedVectors.load("vecs_75_nostop.kv", mmap='r')
    
vectorDictionary = {"vecs_25_":word_vectors_25, "vecs_35_":word_vectors_35, "vecs_45_":word_vectors_45,
                    "vecs_55_":word_vectors_55, "vecs_65_":word_vectors_65, "vecs_75_":word_vectors_75}

distanceFunctionDictionary = {"head_to_head_":headToHead}

print("Vectors Loaded")

documents = pickle.load(open(inFile,'rb'))

for string, vector in vectorDictionary.items():
    word_vectors = vector
    fileDictionary = {}
    for functionName, function in distanceFunctionDictionary.items():
        vectorsArray = []
        for file in range(0,99):    
            for i in range(0,len(documents[file])-1):
                if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
                    vector1 = word_vectors[documents[file][i]]
                    newVector1 = []
                    for k in range(0,len(vector1)):
                            newVector1.append(int(vector1[k]))  
                    vector2 = word_vectors[documents[file][i+1]]
                    newVector2 = []
                    for j in range(0,len(vector2)):
                            newVector2.append(int(vector2[j]))   
                    if functionName == "head_to_head_":
                        if len(vectorsArray) == 0:
                            vectorsArray.append(newVector1)
                        vectorBetween = function(newVector1,newVector2)
                        vectorsArray.append(vectorBetween) 
                        fileDictionary[documents[file][i]] = newVector1
                        fileDictionary[documents[file][i+1]] = newVector2                
        with open("pickle_dictionary_"+string+".p", 'wb') as f:  
            pickle.dump(fileDictionary, f)
        f.close()
        with open("vectors_out_"+string+".csv", 'w') as g:
            writer = csv.writer(g)
            writer.writerows(vectorsArray)
        g.close()
