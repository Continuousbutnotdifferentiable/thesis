# imports needed and logging
import csv
import gzip
import gensim 
import logging
import sys
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
 
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Sysarg must be a .txt.gz
inFile  = sys.argv[1]
#outWordVecs = sys.argv[2]
#outFile = sys.argv[3]


def read_input(input_file):
    """This method reads the input file which is in gzip format"""
    
    logging.info("reading file {0}...this may take a while".format(input_file))
    
    with gzip.open (input_file, 'rb') as f:
        for i, line in enumerate (f): 

            if (i%10000==0):
                logging.info ("read {0} reviews".format (i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list (read_input (inFile))
logging.info ("Done reading data file")

#with open(outFile, "w") as f:
#    writer = csv.writer(f)
#    writer.writerows(documents)


model100 = gensim.models.Word2Vec(documents,size=100,window=10,min_count=2,workers=10)
model100.train(documents, total_examples=len(documents), epochs=10)

model200 = gensim.models.Word2Vec(documents,size=200,window=10,min_count=2,workers=10)
model200.train(documents, total_examples=len(documents), epochs=10)

word_vectors_100 = model100.wv
word_vectors_100.save("reviews_vecs_100.kv")

word_vectors_200 = model200.wv
word_vectors_200.save("reviews_vecs_200.kv")