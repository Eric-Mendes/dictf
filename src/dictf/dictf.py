from collections import UserDict


class dictf(UserDict):
    def __getitem__(self, key):
        result = None

        if isinstance(key, (tuple, list, set)):
            key_set = set(key)
            result = self.__class__()
            for k in key_set:
                result[k] = self.data[k]
        else:
            result = self.data[key]

        return result
