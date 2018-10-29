# thesis

working repo for thesis

apparently gensim already downsamples stopwords when its doing the model training.
what this means for me tho is that the distance implementation still needs to strip out stopwords

todo:

write up arithmetic coding eg in python
    file pg 112, pg 132 

do naive compression and decompression

read compression book
    done thru chapter 5

get word variances and find high/low variance words
plot distributions for those words
see if it holds across dimensions(hypothesis: yes)

done:
my_little_python_word2vec - returns kv instances
distance_calculator - calculates pairwise cosine distances
pickler - takes .gz and saves it to a pickle for opening by other files
similarity finder - outputs lists of similar and dissimilar words
distance_vector_compressor - returns vectors for pairwise words, and pickle of dictionary,
txt files for a bunch of distance metrics and different vector dimensions, norms for head_to_head
plots of 25-75 for each metric and across metrics for each dimension
histogram of distribution of vector entries
PDF of individual vector entries

models trained:
stopped 5,10,50,100,150,200
nostop 5,10,25,30,35,40,45,50,55,60,65,70,75,100,150,200

dependencies:
gensim

ORDER OF OPERATIONS TO RUN OUR METHOD:
pickle the txt.gz corpus you're trying to train
build the models using my_little...

Long Term Todo:
Rebuild/Retrain everything using OANC corpus
Pick ideal vector dimension