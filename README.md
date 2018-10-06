# thesis

working repo for thesis

apparently gensim already downsamples stopwords when its doing the model training.
what this means for me tho is that the distance implementation still needs to strip out stopwords

todo:
implement stopword stripping
build stopword free keyed vectors
plot stopword free graphs against stopword "full" graphs

dependencies:
gensim
nltk