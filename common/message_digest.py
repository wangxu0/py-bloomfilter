# -*- encoding: utf-8 -*-

import hashlib
import threading


class MessageDigestUtils(object):
    __md5 = hashlib.md5()
    __charset = "utf-8"
    __lock = threading.Lock()

    @classmethod
    def create_hashes(cls, data, hashes):
        result = [0] * hashes
        k = 0
        salt = 0
        while k < hashes:
            cls.__lock.acquire()
            cls.__md5.update(str(salt).encode(cls.__charset))
            cls.__md5.update(data)
            salt += 1
            digest = bytearray(cls.__md5.hexdigest())
            cls.__lock.release()

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
