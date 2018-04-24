# -*- encoding: utf-8 -*-

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
