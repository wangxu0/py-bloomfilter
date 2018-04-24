from common.bloomfilter import BloomFilter
from bitset.bitset import BitSet


bloomfilter = BloomFilter(0.001, 10000, BitSet())
bloomfilter.add('123')
print(bloomfilter.contains('123'))
print(bloomfilter.contains('456'))

