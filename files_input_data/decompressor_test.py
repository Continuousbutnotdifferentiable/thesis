import pickle
import csv
import sys
import gzip
import logging
import numpy as np

inPickle = sys.argv[1]
inVectors = sys.argv[2]
outFile = inVectors[-12:-4] + "decompressed_" + ".txt"

def head_to_head_undo(vector1,vector2):
    newWord = []
    for i in range(0,len(vector2)):
        newWord.append(vector1[i]+vector2[i])
    return newWord

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

# Convert strings to vectors
for vector in data:
    for item in range(0,len(vector)):
        if vector[item] != "S":
            vector[item] = int(vector[item])

def head_to_head_undo(vector1,vector2):
    newWord = []
    for i in range(0,len(vector1)):
        newWord.append(vector1[i]+vector2[i])
    return newWord

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

# Convert strings to vectors
for vector in data:
    for item in range(0,len(vector)):
        if vector[item] != 'S':
            vector[item] = int(vector[item])

outString = ""
count = 0
for i in range(0,len(data)-1):
    if len(data[i]) > len(data[i+1]):
        successorWordVector = data[i][:-1]
    for word,vector in compressionDictionary.items():
            if np.allclose(successorWordVector,vector,atol=1e-01):
                outString += word + " "
                successorWordVector = head_to_head_undo(successorWordVector,data[i+1])
                count+= 1
                break    
    if count == 10:
        outString += '\n'
    
print (outString)
with open(outFile,"w") as f:
    f.write(outString)
f.close