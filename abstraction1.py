class Fraction(object):
    def __init__(self,n=0,d=1):
        self._numerator=n
        self._denomenator=d

    def getnumerator(self):
        return self._numerator

    def setnumerator(self,n):
        assert type(n)==int
        self._numerator=n

    def getdenomenator(self):
        return self._denomenator

    def setdenomenator(self,d):
        assert type(d)==int
        self._denomenator=d

    def __add__(self,p2):
        assert type(p2)==Fraction, repr(p2)+"is not Fraction"
        x=(self._numerator * p2._denomenator)+(self._denomenator * p2._numerator)
        y=self._denomenator * self._denomenator
        return Fraction(x,y)

    def __sub__(self,p2):
        if type(p2)!=Fraction:
            return False
        x=(self._numerator * p2._denomenator) - (self._denomenator * p2._numerator)
        y=self._denomenator * self._denomenator
        return Fraction(x,y)

    def __eq__(self,p2):
        #if we use == then this function will be called.
        if type(p2)!=Fraction:
            return False
        ##This is for Duck Typing.
        # if not (hasattr(p2,'numerator') and hasattr(p2,'denomenator')):
        #     return False
        x=self._numerator * p2._denomenator
        y=self._denomenator * p2._numerator
        return x==y

    def __lt__(self,p2): #lessthan
        x=self._numerator*p2._denomenator
        y=self._denomenator * p2._numerator
        return x<y

    def __le__(self,p2): #lessthan or equal to
        x=self._numerator*p2._denomenator
        y=self._denomenator * p2._numerator
        return x<=y

    def __gt__(self,p2): #greaterthan
        x=self._numerator*p2._denomenator
        y=self._denomenator * p2._numerator
        return x>y

    def __ge__(self,p2): #greaterthan or equalto
        x=self._numerator*p2._denomenator
        y=self._denomenator * p2._numerator
        return x>=y

    def _mulint(self,p2):
        x=self._numerator * p2
        y=self._denomenator
        return Fraction(x,y)

    def _mulfrac(self,p2):
        x=self._numerator* p2._numerator
        y=self._denomenator * p2._denomenator
        return Fraction(x,y)
 
    def __mul__(self,p2):
        # assert type(p2)==Fraction or type(p2)==int
        assert isinstance(p2,Fraction),'Required Fraction object'
        if type(p2)==int:
            return self._mulint(p2)

    def __rmul__(self,p2):
        # assert type(p2)==Fraction or type(p2)==int
        assert isinstance(p2,Fraction),'Required Fraction object'
        if type(p2)==int:
            return self._mulint(p2)
        return self._mulfrac(p2)


p1=Fraction(1,2)
p2=3
p3=Fraction(5,4)
p4=4
z=p4*p3
print(z._numerator,z._denomenator)
y=p1*p2
print(y._numerator,y._denomenator)


class BinaryFraction(Fraction):

    def __init__(self, k, n):
        assert type(n)==int and n>=0
        super().__init__(k, 2**n)


e=Fraction(1,3)
print(e._numerator,e._denomenator)
f=Fraction(1,'2')
print(e==f)

