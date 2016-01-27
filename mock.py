# -*- coding: utf-8 -*-


class MMock(object):
    def __getattr__(self, item):
        class Mock(object):
            def __init__(self, *args, **kwargs):
                pass

            def __getitem__(self, item):
                return Mock()

            def __setitem__(self, key, value):
                pass

            def __getattr__(self, item):
                return Mock()

            def __call__(self, *args, **kwargs):
                return Mock()

            def __enter__(self):
                return Mock()

            def __exit__(self, exc_type, exc_val, exc_tb):
                return Mock()

            def __iter__(self):
                yield Mock()

            def __contains__(self, item):
                return Mock()

            def __get__(self, instance, owner):
                return Mock()

            def __set__(self):
                pass

            def __del__(self):
                pass

            def __add__(self, other):
                return Mock()

            def __sub__(self, other):
                return Mock()

            def __mod__(self, other):
                return Mock()

            def __mul__(self, other):
                return Mock()

            def __neg__(self):
                return Mock()

            def __nonzero__(self):
                return True

            def __and__(self, other):
                return Mock()

            def __or__(self, other):
                return Mock()

            def __abs__(self):
                return Mock()

            def __cmp__(self, other):
                return Mock()

            def __eq__(self, other):
                return Mock()

            def __complex__(self):
                return Mock()

            def __gt__(self, other):
                return Mock()

            def __lt__(self, other):
                return Mock()

            def __len__(self):
                return Mock()

        return Mock()


import sys
sys.modules[__name__] = MMock()
