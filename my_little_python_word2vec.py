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
nostop = sys.argv[2]
50string = "vecs_50"
100string = "vecs_100"
150string = "vecs_150"
200string = "vecs_200"
nostopstring = "_nostop"

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

# Trains 4 models using vector sizes 50, 100, 150, and 200 
model100 = gensim.models.Word2Vec(documents,size=100,window=10,min_count=2,workers=10)
model100.train(documents, total_examples=len(documents), epochs=10)
word_vectors_100 = model100.wv

model150 = gensim.models.Word2Vec(documents,size=150,window=10,min_count=2,workers=10)
model150.train(documents, total_examples=len(documents), epochs=10)
word_vectors_150 = model150.wv


model200 = gensim.models.Word2Vec(documents,size=200,window=10,min_count=2,workers=10)
model200.train(documents, total_examples=len(documents), epochs=10)
word_vectors_200 = model200.wv

if nostop == "nostop";
    word_vectors_100.save(100string+nostop+".kv")
    word_vectors_150.save(150string+nostop+".kv")
    word_vectors_200.save(200string+nostop+".kv")

else:
    word_vectors_100.save(100string+".kv")
    word_vectors_150.save(150string+".kv")
    word_vectors_200.save(200string+".kv")