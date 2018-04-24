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


import hashlib


class MessageDigestUtils(object):
    __charset = "utf-8"

    @classmethod
    def create_hashes(cls, data, hashes):
        md5 = hashlib.md5()
        result = [0] * hashes
        k = 0
        salt = 0
        while k < hashes:
            md5.update(str(salt).encode(cls.__charset))
            md5.update(data)
            salt += 1
            digest = bytearray(md5.hexdigest())

            i = 0
            while i < len(digest) / 4 and k < hashes:
                h = 0
                j = i * 4
                while j < ((i * 4) + 4):
                    h <<= 8
                    h |= (digest[j]) & 0xFF
                    j += 1
                result[k] = h
                k += 1
                i += 1
        return result
