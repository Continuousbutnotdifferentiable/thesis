import gensim
import pickle
import csv
import sys
import gzip
import logging
import numpy
from scipy.spatial import distance
from gensim.models import KeyedVectors

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def headToHead(word1,word2):
    newVec = []
    for i in range(0,len(word1)):
        newVec.append(word2[i]-word1[i])
    return newVec


nostop = True
inFile = sys.argv[2]
if nostop:
    word_vectors_25 = KeyedVectors.load("vecs_25_nostop.kv", mmap='r')
    word_vectors_30 = KeyedVectors.load("vecs_30_nostop.kv", mmap='r')
    word_vectors_35 = KeyedVectors.load("vecs_35_nostop.kv", mmap='r')
    word_vectors_40 = KeyedVectors.load("vecs_40_nostop.kv", mmap='r')
    word_vectors_45 = KeyedVectors.load("vecs_45_nostop.kv", mmap='r')
    word_vectors_50 = KeyedVectors.load("vecs_50_nostop.kv", mmap='r')
    word_vectors_55 = KeyedVectors.load("vecs_55_nostop.kv", mmap='r')
    word_vectors_60 = KeyedVectors.load("vecs_60_nostop.kv", mmap='r')
    word_vectors_65 = KeyedVectors.load("vecs_65_nostop.kv", mmap='r')
    word_vectors_70 = KeyedVectors.load("vecs_70_nostop.kv", mmap='r')
    word_vectors_75 = KeyedVectors.load("vecs_75_nostop.kv", mmap='r')
    
vectorDictionary = {"vecs_25_":word_vectors_25, "vecs_30_":word_vectors_30,"vecs_35_":word_vectors_35,
                    "vecs_40_":word_vectors_40, "vecs_45_":word_vectors_45,"vecs_50_":word_vectors_50,
                    "vecs_55_":word_vectors_55, "vecs_60_":word_vectors_60,"vecs_65_":word_vectors_65,
                    "vecs_70_":word_vectors_70, "vecs_75_":word_vectors_75}

distanceFunctionDictionary = {"mahalanobis_":distance.mahalanobis}

print("Vectors Loaded")

documents = pickle.load(open(inFile,'rb'))

for string, vector in vectorDictionary.items():
    word_vectors = vector
    fileDictionary = {}
    for functionName, function in distanceFunctionDictionary.items():
        fileArray = []
        vectorArray = []
        for file in range(0,999):
            for i in range(0,len(documents[file])-1):
                if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
                    vector1 = word_vectors[documents[file][i]] 
                    if vector1 not in vectorArray:
                        vectorArray.append(vector1)
                    vector2 = word_vectors[documents[file][i+1]] 
                    if vector2 not in vectorArray:
                        vectorArray.append(vector2)
        stacked = numpy.vstack(vectorArray)
        iv = numpy.cov(stacked)                   
        for file in range(0,999):
            for i in range(0,len(documents[file])-1):
                if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
                    vector1 = word_vectors[documents[file][i]] 
                    vector2 = word_vectors[documents[file][i+1]]
                    fileArray.append(function(vector1,vector2,iv))
                    
                                           
        with open(functionName+string+".txt","w") as f:
            for item in fileArray:
                f.write("%s\n" % item)
        f.close()
