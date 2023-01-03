
from hashlib import sha1
import numpy as np

from numpy import array
from numpy.linalg import norm

from datasketch.minhash import MinHash
from datasketch.weighted_minhash import WeightedMinHashGenerator
from datasketch.lsh import MinHashLSH

set1 = set(['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
            'estimating', 'the', 'similarity', 'between', 'datasets'])
set2 = set(['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
            'estimating', 'the', 'similarity', 'between', 'documents'])
set3 = set(['minhash', 'is', 'probability', 'data', 'structure', 'for',
            'estimating', 'the', 'similarity', 'between', 'documents'])

m1 = MinHash(num_perm=128)
m2 = MinHash(num_perm=128)
m3 = MinHash(num_perm=128)
for d in set1:
    m1.update(d.encode('utf8'))
for d in set2:
    m2.update(d.encode('utf8'))
for d in set3:
    m3.update(d.encode('utf8'))

# Create LSH index
lsh = MinHashLSH(threshold=0.5, num_perm=128)
#lsh.insert("m1", m1)
lsh.insert("m2", m2)
lsh.insert("m3", m3)

print("Estimated Jaccard m1, m2", m1.jaccard(m2))
print("Estimated Jaccard m1, m3", m1.jaccard(m3))
print("Estimated Jaccard m1, m1", m1.jaccard(m1))

print("Estimated Cosine m1, m2", m1.cosine(m2))
print("Estimated Cosine m1, m3", m1.cosine(m3))
print("Estimated Cosine m1, m1", m1.cosine(m1))

print("Estimated Correlation m1, m2", m1.correlation(m2))
print("Estimated Correlation m1, m3", m1.correlation(m3))
print("Estimated Correlation m1, m1", m1.correlation(m1))

print("Estimated Euclidean m1, m2", m1.euclidean(m2))
print("Estimated Euclidean m1, m3", m1.euclidean(m3))
print("Estimated Euclidean m1, m1", m1.euclidean(m1))


#result = lsh.query(m1)
#print("Approximate neighbours with Jaccard similarity > 0.5", result)