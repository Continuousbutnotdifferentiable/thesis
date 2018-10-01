# thesis
load keyed vectors
fname = get_tmpfile("vectors.kv")
>>> word_vectors.save(fname)
>>> word_vectors = KeyedVectors.load(fname, mmap='r')