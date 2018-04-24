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


import math

from bitset.base_bitset import BaseBitSet
from message_digest import MessageDigestUtils


class BloomFilter(object):
    __charset = "utf-8"

    def __init__(self, false_positive_probability, expected_number_of_elements, bitset):
        if isinstance(bitset, BaseBitSet):
            self.__bitset = bitset
        else:
            raise Exception('Bitset must is instance of BaseBitSet')
        self.__expected_number_of_filter_elements = expected_number_of_elements
        self.__k = int(math.ceil(-(math.log(false_positive_probability) / math.log(2.0))))
        self.__bits_per_element = math.ceil(-(math.log(false_positive_probability) / math.log(2.0))) / math.log(2.0)
        self.__bitset_size = math.ceil((math.ceil(-(math.log(false_positive_probability) / math.log(2.0))) / math.log(
            2.0)) * expected_number_of_elements)
        self.__number_of_added_elements = 0

    def get_false_positive_probability(self, number_of_elements):
        return math.pow((1 - math.exp(-self.__k * number_of_elements / self.__bitset_size)), self.__k)

    def expected_false_positive_probability(self):
        return self.get_false_positive_probability(self.__expected_number_of_filter_elements)

    def get_false_positive_probability(self):
        return self.get_false_positive_probability(self.__number_of_added_elements)

    def get_k(self):
        return self.__k

    def clear_all(self):
        self.__bitset.clear()

    def add(self, element):
        hashes = MessageDigestUtils.create_hashes(element.encode(self.__charset), self.__k)
        for hash in hashes:
            self.__bitset.set_bit(abs(int(hash % self.__bitset_size)))
        self.__number_of_added_elements += 1

    def add_all(self, elements):
        for element in elements:
            self.add(element)

    def contains(self, element):
        hashes = MessageDigestUtils.create_hashes(element, self.__k)
        for hash in hashes:
            if not self.__bitset.get_bit(abs(int(hash % self.__bitset_size))):
                return False
        return True

    def contains_all(self, elements):
        for element in elements:
            if not self.contains(element):
                return False
        return True

    def get_bit(self, bit_index):
        return self.__bitset.get_bit(bit_index)

    def set_bit(self, bit_index, value=True):
        self.__bitset.set_bit(bit_index, value)

    def get_bitset(self):
        return self.__bitset

    def get_bitset_size(self):
        return self.__bitset_size

    def count(self):
        return self.__number_of_added_elements

    def is_empty(self):
        return self.count() <= 0

    def get_expected_number_of_filter_elements(self):
        return self.__expected_number_of_filter_elements

    def get_expected_bits_per_element(self):
        return self.__bits_per_element

    def get_bits_per_element(self):
        return self.__bitset_size / self.__number_of_added_elements
