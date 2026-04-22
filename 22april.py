#class abc:
 #   val=10
   # def __init__(self,val):
      #  print("welcome to python")
     #   self.val=val
    #    print("total strength is",self.val)
#obj=abc(36)

#class abc:
   # C_val=10
    #def __init__(self,val):
   #      self.val=val
 #       print("the value 1 is",self.val)
#        print("the value 2 is",abc.C_val)
#obj=abc(36)
#find whether it is even or odd
class number:
    def __init__(self,number):
        self.number=number
    def even_odd(self):
        if self.number%2==0:
            print("the number is even")
        else:
            print("the number is odd")
obj=number(36)
obj.even_odd()