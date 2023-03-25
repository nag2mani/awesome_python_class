class Date(object):
    """
    A class representing a month, day and year
    Attribute MONTHS: A CLASS ATTRIBUTE list of all month abbreviations in order
    Attribute DAYS: A CLASS ATTRIBUTE that is a dictionary.Keys are the strings from MONTHS;
    values are days in that month ('Feb' is 28 days)
    """
    # Attribute _year: The represented year. An int >= 2000 (IMMUTABLE)
    # Attribute _month: The month. A valid 3-letter string from MONTHS (IMMUTABLE)
    # Attribute _day: The day. An int representing a valid day of _month (MUTABLE)

    MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    DAYS = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}

    def isleapyear(self):
        first=str(self._year)[2:4]
        last=str(self._year)[:2]
        if first!='00':
            if int(first)%4==0:
                return True
            else:
                return False
        else:
            if int(last)%4==0:
                return True
            else:
                return False

    def getyear(self):
        return self._year

    def getmonth(self):
        return self._month

    def getday(self):
        return self._day

    def setday(self,value):
        assert type(value)==int,'Not a valid day'
        if self.isleapyear():
            if self._month=='Feb':
                assert 1<=value>=29,"Not a valid day"
                self._day=value
        else:
            assert 1<=value<=Date.DAYS[self._month], 'Not a valid day'
            self._day=value


    def __init__(self,y,m,d):
        """Initializes a new date for the given month, day, and year
        Precondition: y is an int >= 2000 for the year
        Precondition: m is a 3-letter string for a valid month
        Precondition: d is an int and a valid day for month m"""
        # assert isinstance(_year,int),"Not a valid year"
        assert type(y)==int and y>=2000, "Year should be int and >=2000"
        assert m in Date.MONTHS, "Months should be valid"
        self._year=y
        self._month=m
        self.setday(d)

    def __str__(self):
        """Returns a string representation of this date.
        The representation is month day, year like this: 'Jan 2, 2002' """
        return str(self._month) +" "+ str(self._day)+" ,"+str(self._year)


    def __lt__(self, other):
        """Returns True if this date happened before other (False otherwise)
        Precondition: other is a Date
        This method causes a TypeError if the precondition is violated."""
	
        assert isinstance(other, Date),"Not a valid date"
	
        if self._year < other._year:
            return True
        elif self._year==self._year:
            if self._month==other._month:
                return self._day < other._day
            else:
                 return Date.MONTHS.index(self._month) < Date.MONTHS.index(other._month)


class DateTime(Date):
	"""A class representing a month, day and year, plus time of day (hours,
	minutes)"""
	# Attribute _hour: The hour of the day. An int in range 0..23 (MUTABLE)
	# Attribute _minute: The minute of the hour. An int in range 0..59 (MUTABLE)

	def gethour(self):
		return self._hour

	def sethour(self, h):
		assert isinstance(h, int), repr(h) + 'is not a valid hour'
		assert 0 <= h <= 23, repr(h) + 'is not a valid hour'
		self._hour = h

	def getminute(self):
		return self._minute

	def setminute(self, m):
		assert isinstance(m, int), repr(m) + 'is not a valid minute'
		assert 0 <= m <= 59, repr(m) + 'is not a valid minute'
		self._minute = m

	def __init__(self, y, m, d, h = 0, min = 0):
		super().__init__(y, m, d)
		self.sethour(h)
		self.setminute(min)

	def __str__(self):
		if self._minute < 10:
			return  str(self._hour) + ':0' + str(self._minute) + ' on ' + super().__str__()
		return  str(self._hour) + ':' + str(self._minute) + ' on ' + super().__str__()


d1 = DateTime(2200, 'Feb', 27, 8, 56)
d2 = DateTime(2025, 'Feb', 28, 8, 6)
print(d1>d2)
print(str(d1))
print(str(d2))
print(d1._month, d1._year, d1._hour, d1._minute)



