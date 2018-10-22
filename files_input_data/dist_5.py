import gensim
import sys
import gzip
import logging
from gensim.models import KeyedVectors

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# List of ntlkStopwords current as of July 6, 2018
ntlkStopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'youre', 'youve', 'youll', 'youd', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'shes', 'her', 'hers', 'herself', 'it', 'its', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'thatll', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'dont', 'should', 'shouldve', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'arent', 'couldn', 'couldnt', 'didn', 'didnt', 'doesn', 'doesnt', 'hadn', 'hadnt', 'hasn', 'hasnt', 'haven', 'havent', 'isn', 'isnt', 'ma', 'mightn', 'mightnt', 'mustn', 'mustnt', 'needn', 'neednt', 'shan', 'shant', 'shouldn', 'shouldnt', 'wasn', 'wasnt', 'weren', 'werent', 'won', 'wont', 'wouldn', 'wouldnt']

nostop = True
inFile = sys.argv[2]

if nostop:
    word_vectors_50 = KeyedVectors.load("vecs_5_nostop.kv", mmap='r')
    word_vectors_100 = KeyedVectors.load("vecs_10_nostop.kv", mmap='r')

if not nostop:
    word_vectors_50 = KeyedVectors.load("vecs_5.kv", mmap='r')
    word_vectors_100 = KeyedVectors.load("vecs_10.kv", mmap='r')
    
print("Vectors Loaded")

def read_input(input_file):
    """This function reads the input file which is in gzip format"""
    
    logging.info("reading file {0}...this may take a while".format(input_file))
    
    with gzip.open (input_file, 'rb') as f:
        for i, line in enumerate (f): 

            if (i%10000==0):
                logging.info ("read {0} reviews".format (i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

documents = list (read_input (inFile))


# If nostop parameter is true, strip the stopwords if they're in the document and in the ntlkStopwords list
if nostop:
    for doc in documents:
        for word in doc:
            if word in ntlkStopwords:
                doc.remove(word)

# Distances internal 10000
# forms list of lists of distances from valid word cosine similarities
distancesInternal10000 = []
distancesInternalJoined10000 = []
word_vectors = word_vectors_50
for file in range(0,9999):
    fileList = []
    for i in range(0,len(documents[file])-1):
        if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
            fileList.append(word_vectors.similarity(documents[file][i],documents[file][i+1]))
    distancesInternal10000.append(fileList)

for lists in distancesInternal10000:
    for item in lists:
        item = abs(item)
        distancesInternalJoined10000.append(item)

distancesInternalJoined10000.sort()

if nostop:
    with open("distance10000_5_nostop.txt",'w') as f:
        for item in distancesInternalJoined10000:
                f.write("%s\n" % item)
else:
    with open("distance10000_5.txt",'w') as f:
        for item in distancesInternalJoined10000:
                f.write("%s\n" % item)


# 10000, word vecs_10

distancesInternal10000 = []
distancesInternalJoined10000 = []
word_vectors = word_vectors_100
for file in range(0,9999):
    fileList = []
    for i in range(0,len(documents[file])-1):
        if documents[file][i] in word_vectors.vocab and documents[file][i+1] in word_vectors.vocab:
            fileList.append(word_vectors.similarity(documents[file][i],documents[file][i+1]))
    distancesInternal10000.append(fileList)

for lists in distancesInternal10000:
    for item in lists:
        item = abs(item)
        distancesInternalJoined10000.append(item)

distancesInternalJoined10000.sort()

if nostop:
    with open("distance10000_10_nostop.txt",'w') as f:
        for item in distancesInternalJoined10000:
                f.write("%s\n" % item)
else:
    with open("distance10000_10.txt",'w') as f:
        for item in distancesInternalJoined10000:
                f.write("%s\n" % item)