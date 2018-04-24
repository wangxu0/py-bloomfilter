# -*- encoding: utf-8 -*-

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from base_bitset import BaseBitSet


class BitSet(BaseBitSet):

    def __init__(self):
        """
        init bit set
        """
        self.__bits = 0L

    def set_bit(self, bit_index, value=True):
        """
        Set a single bit in the Bloom filter, value default is true.
        :param bit_index: bit index.
        :param value: True default
        :return: void
        """
        if value:
            self.__bits |= (1 << bit_index)
        else:
            self.clear(bit_index)

    def get_bit(self, bit_index):
        """
        Return the bit set used to store the Bloom filter.
        :param bit_index: bit index.
        :return: the bit set used to store the Bloom filter.
        """
        if (self.__bits & (1 << bit_index)) != 0:
            return True
        else:
            return False

    def clear(self, bit_index):
        """
        Clear the bit set on the index, so the bit set value is false on index.
        :param bit_index: bit index.
        :return: void
        """
        self.__bits &= ~(1 << bit_index)

    def clear_all(self):
        """
        Clear the bit set, so the bit set value is all false.
        :return: void
        """
        self.__bits = 0L

    def count(self):
        """
        Returns the number of bits in the Bloom filter.
        :return: the number of bits in the Bloom filter.
        """
        count = 0
        temp_bits = self.__bits
        while temp_bits != 0:
            temp_bits &= (temp_bits - 1)
            count = count + 1
        return count

    def is_empty(self):
        """
        Returns is the bit set empty, bit set is empty means no any elements added to bit set.
        :return: is the bit set empty.
        """
        return self.count() <= 0

