# -*- encoding: utf-8 -*-


class BaseBitSet(object):

    def set_bit(self, bit_index, value=True):
        """
        Set a single bit in the Bloom filter, value is true or false.
        :param bit_index: bit index.
        :param value:
        :return: void
        """

    def get_bit(self, bit_index):
        """
        Return the bit set used to store the Bloom filter.
        :param bit_index: bit index.
        :return: the bit set used to store the Bloom filter.
        """

    def clear(self, bit_index):
        """
        Clear the bit set on the index, so the bit set value is false on index.
        :param bit_index: bit index.
        :return: void
        """

    def clear_all(self):
        """
        Clear the bit set, so the bit set value is all false.
        :return: void
        """

    def count(self):
        """
        Returns the number of bits in the Bloom filter.
        :return: the number of bits in the Bloom filter.
        """

    def is_empty(self):
        """
        Returns is the bit set empty, bit set is empty means no any elements added to bit set.
        :return: is the bit set empty.
        """