# imports needed and logging
import gzip
import gensim 
import logging
import sys
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
 
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Sysarg must be a .txt.gz
data_file  = sys.argv[1]

# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list (read_input (data_file))
logging.info ("Done reading data file")

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
documents = list (read_input (data_file))
logging.info ("Done reading data file")

model = gensim.models.Word2Vec(documents,size=150,window=10,min_count=2,workers=10)
model.train(documents, total_examples=len(documents), epochs=10)

fname = "reviews_data.kv" 
word_vectors = model.wv
word_vectors.save(fname)
distances = []
for i in documents:
    for j in i:
        distances.append()
 
