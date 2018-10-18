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
    word_vectors_50 = KeyedVectors.load("vecs_50_nostop.kv", mmap='r')
    vectorList = [word_vectors_50]

if not nostop:
    word_vectors_50 = KeyedVectors.load("vecs_50.kv", mmap='r')
    vectorList = [word_vectors_50]
print("Vectors Loaded")

fileObject = open(inFile,'r')  
documents = pickle.load(fileObject)

