# Variant 1

class MyDict(dict):
    def __init__(self, d):
        self._d = d if d is not None else {}

    def str_keys(self):
        return "".join(self._d.keys())


d1 = {
    "abc": [1, 2, 3],
    "def": [4, 5, 6],
    "klm": [7, 8, 9]
}

d2 = {
    "": [],
    "__": [532, 0],
    ",": [0, 1, 0, -1]
}

d3 = {
    "¯\_": [-1],
    "(ツ)": [0],
    "_/¯": [1]
}


def main():
    md1 = MyDict(d1)
    md2 = MyDict(d2)
    md3 = MyDict(d3)
    assert "abcdefklm" == md1.str_keys()
    assert "__," == md2.str_keys()
    assert "¯\_(ツ)_/¯" == md3.str_keys()

if __name__ == "__main__":
    main()