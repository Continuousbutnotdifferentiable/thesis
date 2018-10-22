# thesis

working repo for thesis

apparently gensim already downsamples stopwords when its doing the model training.
what this means for me tho is that the distance implementation still needs to strip out stopwords

todo:
figure out wtf is going on with strip stopwords??

do naive compression and decompression
plot length of distance vector vs cosine similarity
    add norm print function to elegant distance
plot other metrics for distance
    need to finish malahanorbitonsad
read compression book
    done thru chapter 3

done:
my_little_python_word2vec - returns kv instances
distance_calculator - calculates pairwise cosine distances
pickler - takes .gz and saves it to a pickle for opening by other files
similarity finder - outputs lists of similar and dissimilar words

models trained:
stopped 5,10,50,100,150,200
nostop 5,10,25,30,35,40,45,50,55,60,65,70,75,100,150,200

dependencies:
gensim

ORDER OF OPERATIONS TO RUN OUR METHOD:
pickle the txt.gz corpus you're trying to train
build the models using my_little...