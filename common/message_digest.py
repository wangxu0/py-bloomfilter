# -*- encoding: utf-8 -*-

import hashlib


class MessageDigestUtils(object):

        __md5 = hashlib.md5()
        __charset = "utf-8"

        @classmethod
        def create_hashes(cls, data, hashes):
            result = [0] * hashes
            k = 0
            salt = 0
            while k < hashes:
                cls.__md5.update(salt)
                cls.__md5.update(data)
                salt += 1
                digest = cls.__md5.digest()


