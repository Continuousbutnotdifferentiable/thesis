import pickle
import gensim
import sys
import gzip
import logging

inFile = sys.argv[1]

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

with open('documents.pkl', 'wb') as f:  
    pickle.dump(documents, f)