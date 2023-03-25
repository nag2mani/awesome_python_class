class Length(object):
    @property
    def len(self):
        return self.len
    
    @len.setter
    def len(self, value):
        assert type(value)==int and value>0
        self.len=value
    
    def __init__(self, l):
        self._len=l


class Breadth(object):
    @property
    def bread(self):
        return self._bread

    @bread.setter
    def bread(self, value):
        assert type(value)==int and value>0
        self._bread=value

    def __init__(self, b):
        self._bread=b


class Rect_area(Length, Breadth):

    def __init__(self, l, b):
        # Length(l)
        # Breadth(b)       # creating its own new object not of self.

        # Length.__init__(self, l)   
        # Breadth.__init__(self, b)    #self denote the same of self of init.

        super().__init__()
        super(Length, self).__init__()

    def r_area(self):
        return self.len * self.bread

e=Rect_area(2,3)
print(e.r_area())
print(e.len)

