# imports needed and logging
import csv
import gzip
import gensim 
import logging
import sys
from gensim.parsing.preprocessing import preprocess_string
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
 
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# List of ntlkStopwords current as of July 6, 2018
ntlkStopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'youre', 'youve', 'youll', 'youd', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'shes', 'her', 'hers', 'herself', 'it', 'its', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'thatll', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'dont', 'should', 'shouldve', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'arent', 'couldn', 'couldnt', 'didn', 'didnt', 'doesn', 'doesnt', 'hadn', 'hadnt', 'hasn', 'hasnt', 'haven', 'havent', 'isn', 'isnt', 'ma', 'mightn', 'mightnt', 'mustn', 'mustnt', 'needn', 'neednt', 'shan', 'shant', 'shouldn', 'shouldnt', 'wasn', 'wasnt', 'weren', 'werent', 'won', 'wont', 'wouldn', 'wouldnt']

# Sysarg must be a .txt.gz
nostop = False
inFile  = sys.argv[2]

# Setup string names for file io
string5 = "vecs_5"
string10 = "vecs_10"
nostopstring = "_nostop"

def read_input(input_file):
    """This method reads the input file which is in gzip format"""
    
    logging.info("reading file {0}...this may take a while".format(input_file))
    
    with gzip.open (input_file, 'rb') as f:
        for i, line in enumerate (f): 

            if (i%10000==0):
                logging.info ("read {0} reviews".format (i))
            # do some pre-processing and return a list of words for each review text
            else:
                yield gensim.utils.simple_preprocess (line)

# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list (read_input (inFile))
logging.info ("Done reading data file")

if nostop:
    for doc in documents:
        for word in doc:
            if word in ntlkStopwords:
                doc.remove(word)


# Trains 4 models using vector sizes 50, 100, 150, and 200 
model10 = gensim.models.Word2Vec(documents,size=10,window=10,min_count=2,workers=10)
model10.train(documents, total_examples=len(documents), epochs=10)
word_vectors_10 = model10.wv

model5 = gensim.models.Word2Vec(documents,size=5,window=10,min_count=2,workers=10)
model5.train(documents, total_examples=len(documents), epochs=10)
word_vectors_5 = model5.wv

if nostop:
    word_vectors_5.save(string5+nostopstring+".kv")
    word_vectors_10.save(string10+nostopstring+".kv")

else:
    word_vectors_5.save(string5+".kv")
    word_vectors_10.save(string10+".kv")