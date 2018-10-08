import gensim
import sys
import gzip
import logging
from gensim.models import KeyedVectors
from statistics import mean

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


nostop = sys.argv[1]
inFile = sys.argv[2]

word_vectors_50 = KeyedVectors.load("reviews_vecs_50.kv", mmap='r')
word_vectors_100 = KeyedVectors.load("reviews_vecs_100.kv", mmap='r')
word_vectors_150 = KeyedVectors.load("reviews_vecs_150.kv", mmap='r')
word_vectors_200 = KeyedVectors.load("reviews_vecs_200.kv", mmap='r')
vectorList = [word_vectors_100 , word_vectors_150 , word_vectors_200]
print("Vectors Loaded")

def read_input(input_file):
    """This method reads the input file which is in gzip format"""
    
    logging.info("reading file {0}...this may take a while".format(input_file))
    
    with gzip.open (input_file, 'rb') as f:
        for i, line in enumerate (f): 

            if (i%10000==0):
                logging.info ("read {0} reviews".format (i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

documents = list (read_input (inFile))

distancesInternal10000 = []
distancesInternal20000 = []

# forms list of lists of distances from valid word cosine similarities
for vectors in vectorList:
    word_vectors = vectors
    for file in range(0,9999):
        fileList = []
        for i in range(0,len(documents[file])-1):
            if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
                fileList.append(word_vectors.similarity(documents[file][i],documents[file][i+1]))
        distancesInternal10000.append(fileList)

distancesInternalJoined = []
for lists in distancesInternal:
    for item in lists:
        item = abs(item)
        distancesInternalJoined.append(item)

distancesInternalJoined.sort()

with open("distance10000.txt",'w') as f:
    for item in distancesInternalJoined:
            f.write("%s\n" % item)
with open("distance1.txt",'w') as f:
    for item in distancesInternal[0]:
        f.write("%s\n" % item)
with open("distance2.txt",'w') as f:
    for i in distancesInternal[1]:
        f.write("%s\n" % i)
