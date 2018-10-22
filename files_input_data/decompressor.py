import pickle
import csv
import sys
import gzip
import logging
import numpy

inPickle = sys.argv[1]
inVectors = sys.argv[2]
outFile = inVectors[-12:-4] + "decompressed_" + ".txt"

if inPickle[-2:] != ".p":
    print("First arg must be .p (pickle) file.")
    sys.exit(-1)

if inVectors[-4:] != ".csv":
    print("Second arg must be .csv file.")
    sys.exit(-1)
# Load the pickled dictionary
compressionDictionary = pickle.load(open(inPickle,'rb'))

with open(inVectors,"r") as f:
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=','))
f.close()

outString = ""
count = 0
for vec in data:
    for string, vector in compressionDictionary.items():
        if vec == vector:
            words = string.split()
            outString+= (words[0]+' ')
            count += 1
        if count == 12:
            outString+= "\n"
            count = 0

with open(outFile,"w") as f:
    f.write(outString)
f.close


