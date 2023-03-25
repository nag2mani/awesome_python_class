#Question 1
def fun():
      try:
         a=float(input("number :"))
         assert a<4
         b = a/(a-3)
         print("Value of b = ", b)
      except ZeroDivisionError:
         print("We can't divide by 0")
      except TypeError:
         print("input should be int or float")
      except ValueError:
          print("Can't convert string to int or float")
      except AssertionError:
          print("out of range")
fun()



# Question 2
"""
ValueError: is a built-in Python exception class that is raised whenever an operation or function 
receives an argument that has the right type but an inappropriate value.
TypeError: is an exception that occurs when the data type of objects in an operation is inappropriate.
"""

class Error(Exception):
    pass

class ZError(Error):
    pass

class RError(Error):
    pass

try:
    num = int(input("Enter a number: "))
    if num == 0:
        raise ZError
    if num < 0:
        raise RError
except ZError:
    print("you can't divide with 0")
except RError:
    print("You can't put Negative")
except ValueError:
    print("input can't convert to int")



##Question 3
class MyError(Exception):
    
    def __init__(self, value):
      self._value = value
    # pass

    def __str__(self):
        return(repr(self.value))
try:
    raise MyError(3*2)
# Value of Exception is stored in error

except MyError as error:
    print('A New Exception occurred: ', error._value)

# print('A New Exception occurred: ', error.value)














# # 1.	Observe the types of errors the following code can possibly generate. Now handle the errors suitably by enclosing calls to the function inside a try block.

# """
# def fun(a):
#     if a < 4:
#         b = a/(a-3)

#     print("Value of b = ", b)

# try:
# 	print(fun(0))
# except ZeroDivisionError:
# 	print('Hey , the number you gave is getting divided by 0')
# except ValueError:
# 	print('Hey, number is out of range')
# except:
# 	print('Hey, type of number is not int')
# except UnboundLocalError:   # aslo called name error
# 	print('Hey, number you gave is not able to calculate any thing but used befor giving any value to it.')

# """

# """

# # 3.	What would be the output of the following lines of code?

# class MyError(Exception):

#     # Constructor or Initializer
#     def _init_(self, value):
#     	pass
#         # self.value = value

#     # _str_ is to print() the value
#     def _str_(self):
#         return(repr(self.value))

# # raise(MyError(3*2))
# try:
#     raise(MyError(3*2))

# # Value of Exception is stored in error
# except MyError as error:
#     print('A New Exception occurred: ', error.value)

# # Now comment out the only line of code inside the initializer and replace it with pass.
# # Try to have the value in the following statement printed.
# # print('A New Exception occurred: ', error.value)


# """

# class Error(Exception):
# 	pass

# class ZError(Error):
# 	pass


# class RError(Error):
# 	pass


# try:
# 	num=int(input("Enter number"))
# 	# num=int(-6)

# 	# raise ZError
# 	# ZeroDivisionError=ZError
# 	# ZError=ZeroDivisionError
# 	# ZError=ZeroDivisionError
# 	# ZError=RError
# 	# RError=ZError

# 	# num='l'
# 	# d= 8/num
# 	if num == 0:
# 		raise ZError
# 		# raise RError
# 	if num < 0:
# 		raise RError

# except ZError:
# 	print('Hey,given number is 0, try again')
# except RError:
# 	print('Hey, given number is less than 0, try again')
# print('given input type can not be converted into intger ')
