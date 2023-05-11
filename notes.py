class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Desc:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if self.name == '_name':
            if value in ["до", "ре", "ми", "фа", "соль", "ля", "си"]:
                instance.__dict__[self.name] = value
            else:
                raise ValueError
        elif self.name == '_ton':
            if value in [-1, 0, 1]:
                instance.__dict__[self.name] = value
            else:
                raise ValueError

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Note:
    name = Desc()
    ton = Desc()

    def __init__(self, name, ton):
        self.name = name
        self.ton = ton


class Notes(Singleton):
    __slots__ = ['_do', '_re', '_mi', '_fa', '_solt', '_la', '_si']

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note('ре', 0)
        self._mi = Note('ми', 0)
        self._fa = Note('фа', 0)
        self._solt = Note('соль', 0)
        self._la = Note('ля', 0)
        self._si = Note('си', 0)

    def __getitem__(self, item):
        if 0 <= item <= 6:
            return getattr(self, self.__slots__[item])
        else:
            raise IndexError


notes = Notes()
# do = notes[0]
# do._ton = 1
# re = notes[1]
# mi = notes[2]
# fa = notes[3]
# solt = notes[4]
# la = notes[5]
# si = notes[6]
#
# print(do.__dict__, re.__dict__, mi.__dict__, fa.__dict__, solt.__dict__, la.__dict__, si.__dict__, sep='\n')
