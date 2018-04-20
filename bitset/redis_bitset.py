# -*- encoding: utf-8 -*-

from base_bitset import BaseBitSet


class RedisBitSet(BaseBitSet):

    def __init__(self, name, redis_client):
        """
        init redis bitset
        """
        self.__name = name
        self.__redis_client = redis_client

    def set_bit(self, bit_index, value=True):
        """
        Set a single bit in the Bloom filter, value is true or false.
        :param bit_index: bit index.
        :param value:
        :return: void
        """
        self.__redis_client.setbit(self.__name, bit_index, value)

    def get_bit(self, bit_index):
        """
        Return the bit set used to store the Bloom filter.
        :param bit_index: bit index.
        :return: the bit set used to store the Bloom filter.
        """
        return self.__redis_client.getbit(self.__name, bit_index)

    def clear(self, bit_index):
        """
        Clear the bit set on the index, so the bit set value is false on index.
        :param bit_index: bit index.
        :return: void
        """
        self.__redis_client.setbit(self.__name, bit_index, 0)

    def clear_all(self):
        """
        Clear the bit set, so the bit set value is all false.
        :return: void
        """
        self.__redis_client.delete(self.__name)

    def count(self):
        """
        Returns the number of bits in the Bloom filter.
        :return: the number of bits in the Bloom filter.
        """
        return self.__redis_client.bitcount()

    def is_empty(self):
        """
        Returns is the bit set empty, bit set is empty means no any elements added to bit set.
        :return: is the bit set empty.
        """
        return self.count() <= 0

