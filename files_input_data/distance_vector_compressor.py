import gensim
import pickle
import csv
import sys
import gzip
import logging
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

distanceFunctionDictionary = {"bray_curtis_":distance.braycurtis,"canberra_":distance.canberra,"chebyshev_":distance.chebyshev,
                                "city_block_":distance.cityblock, "correlation_":distance.correlation, "cosine_":distance.cosine,
                                "euclidian_":distance.euclidean, "mahalanobis_":distance.mahalanobis,"minowski_":distance.minkowski,
                                "sqeuclidian_":distance.sqeuclidean,"head_to_head_":headToHead}

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
                    vector2 = word_vectors[documents[file][i+1]] 
                    if functionName == "head_to_head_":
                        words = documents[file][i] + " " + documents[file][i+1]
                        vectorBetween = function(vector1,vector2)
                        vectorArray.append(vectorBetween)
                        fileDictionary[words] = vectorBetween
                    if functionName == "mahalanobis_":
                        fileArray.append(vector1)
                        fileArray.append(vector2)
                    elif functionName != "head_to_head_" or functionName == "mahalanobis_":
                        fileArray.append(function(vector1,vector2))
        fileArray.sort()
        if functionName == "head_to_head_":
            with open(functionName+string+".csv","w") as f:
                writer = csv.writer(f)
                writer.writerows(vectorArray)
            f.close()
            with open(functionName+string+".p","wb") as f:
                pickle.dump(fileDictionary, f)
            f.close()
        else:
            with open(functionName+string+".txt","w") as f:
                for item in fileArray:
                    f.write("%s\n" % item)
            f.close()
