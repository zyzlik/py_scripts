class AbandonClass:

    def __new__(cls, value):
        if value:
            return super(AbandonClass, cls).__new__(cls)
        else:
            raise ValueError

    def __init__(self, value):
        self.value = value

    def test_method(self):
        print self.value

a = AbandonClass(True)
b = AbandonClass(False)
