from common.bloomfilter import BloomFilter
from bitset.bitset import BitSet
from bitset.redis_bitset import RedisBitSet

# bitset
bloomfilter = BloomFilter(0.001, 10000, BitSet())
bloomfilter.add('123')
print(bloomfilter.contains('123'))
print(bloomfilter.contains('456'))

# redis bitset
bloomfilter2 = BloomFilter(0.001, 10000, RedisBitSet())
bloomfilter2.add('123')
print(bloomfilter2.contains('123'))
print(bloomfilter2.contains('456'))

