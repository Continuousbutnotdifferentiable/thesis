import gensim
import sys
import gzip
import logging
from gensim.models import KeyedVectors
from statistics import mean
from gensim.parsing.preprocessing import remove_stopwords

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

vecs_100 = 'reviews_vecs_100_nostop'
vecs_150 = 'reviews_vecs_150_nostop'
inFile = sys.argv[1]
word_vectors_100 = KeyedVectors.load(vecs_100+'.kv', mmap='r')
word_vectors_150 = KeyedVectors.load("reviews_vecs_150_nostop.kv", mmap='r')
word_vectors_200 = KeyedVectors.load("reviews_vecs_200_nostop.kv", mmap='r')
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
            yield gensim.utils.simple_preprocess (remove_stopwords(line))

documents = list (read_input (inFile))

distancesInternal = []

# forms list of lists of distances from valid word cosine similarities
for vectors in vectorList:
    word_vectors = i
    minlist
    for file in range(0,9999):
        fileList = []
        for i in range(0,len(documents[file])-1):
            if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
                fileList.append(word_vectors.similarity(documents[file][i],documents[file][i+1]))
        distancesInternal.append(fileList)
        if len(fileList) != 0:
            distancesAcross.append((sum(fileList)/float(len(fileList))))

distancesInternalJoined = []
for lists in distancesInternal:
    for item in lists:
        if item < 0:
            item = -item
        distancesInternalJoined.append(item)

distancesInternalJoined.sort()

with open("distance10000_150_nostop.txt",'w') as f:
    for item in distancesInternalJoined:
            f.write("%s\n" % item)