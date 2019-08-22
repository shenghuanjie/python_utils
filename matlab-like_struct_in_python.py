class MatlabStruct():

    def __getitem__(self, key):
        if isinstance(key, str):
            return getattr(self, key)
        elif isinstance(key, int) or isinstance(key, tuple) or isinstance(key, slice):
            result = {}
            for k, v in self.__dict__.items():
                result[k] = v[key]
            return result
        else:
            print(key)
            raise ValueError

    def __setitem__(self, key, value):
        if isinstance(key, str):
            setattr(self, key, value)
        elif isinstance(key, int) or isinstance(key, tuple) or isinstance(key, slice):
            i = 0
            for k, v in self.__dict__.items():
                if isinstance(value, dict):
                    if k in value:
                        attr = getattr(self, k)
                        attr[key] = value[k]
                elif isinstance(value, list):
                    attr = getattr(self, k)
                    attr[key] = value[i]
                    i = i + 1
                else:
                    attr = getattr(self, k)
                    attr[key] = value
        else:
            raise ValueError
