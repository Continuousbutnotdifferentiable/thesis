import gensim
import pickle
import sys
import gzip
import logging
from gensim.models import KeyedVectors

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# List of ntlkStopwords current as of July 6, 2018

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

print("Vectors Loaded")

fileObject = open(inFile,'r')  
documents = pickle.load(fileObject)

for string, vector in vectorDictionary:
    theVectors = word_vectors
    for file in range(0,99):
        fileList = []
        for i in range(0,len(documents[file])-1):
            if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
                
        distancesInternal10000.append(fileList)


tipToTail(word1,word2):