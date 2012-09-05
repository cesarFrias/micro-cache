# coding=utf-8

class MicroCache(object):

    def __init__(self):
        self.collections = {}

    def __call__(self, *args, **kwargs):
        return self.get(*args, **kwargs)

    def __getitem__(self, item):
        return self.get(item)

    def set(self, key, value, timeout=None):
        """
        Timeout will not be used
        """
        self.collections[key] = value

    def get(self, key, value=None):
        if not self.collections.has_key(key) and value:
            self.update(key, value)
        return self.collections[key]

    def update(self, key, value):
        if hasattr(value, '__call__'):
            self.collections[key] = value()
        else:
            self.collections[key] = value

    def remove(self, key):
        del self.collections[key]

    def close(self):
        self.collections.clear()

    def clear(self):
        self.close()
