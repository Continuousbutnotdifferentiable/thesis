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
    
vectorDictionary = {"vecs_25_":word_vectors_25}

distanceFunctionDictionary = {"head_to_head_":headToHead}

print("Vectors Loaded")

documents = pickle.load(open(inFile,'rb'))

for string, vector in vectorDictionary.items():
    word_vectors = vector
    fileDictionary = {}
    count = 0 
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
                    while count < 5:
                        print (i, " "+ documents[file][i]+ " ", newVector1,"\n")
                        print (i+1, " "+ documents[file][i+1]+ " ", newVector2,"\n")
                        print ("count = ", count, "\n")
                        count += 1
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
