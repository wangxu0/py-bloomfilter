# -*- encoding: utf-8 -*-

import hashlib


class MessageDigestUtils:

        __md5 = hashlib.md5()
        __charset = "utf-8"

        @classmethod
        def create_hashes(cls, data, hashes):
            result = [0] * hashes
            k = 0
            salt = 0
            while k < hashes:
                

