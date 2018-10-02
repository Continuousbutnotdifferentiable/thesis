import gensim
import sys
import gzip
import logging
from gensim.models import KeyedVectors
from statistics import mean

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


inFile = sys.argv[1]
outFile = sys.argv[2]
word_vectors = KeyedVectors.load("reviews_vecs.kv", mmap='r')
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

distancesInternal = []
distancesAcross = []

for file in range(0,9999):
    fileList = []
    for i in range(0,len(documents[file])-1):
        if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
            fileList.append(word_vectors.similarity(documents[file][i],documents[file][i+1]))
    distancesInternal.append(fileList)
    if len(fileList) != 0:
        distancesAcross.append((sum(fileList)/float(len(fileList))))



with open("meanAcross.txt", 'w') as f:
    for item in distancesAcross:
        f.write("%s\n" % item)
with open("distance10000.txt",'w') as f:
    for item in distancesInternal:
        for j in item:
            f.write("%s\n" % j)
with open("distance1.txt",'w') as f:
    for i in distancesInternal[0]:
        f.write("%s\n" % i)
with open("distance2.txt",'w') as f:
    for i in distancesInternal[1p]:
        f.write("%s\n" % i)
