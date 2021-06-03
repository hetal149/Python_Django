#calculate sum of three numbers
class cal1:
    def selfdata(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
    def declare(self):
        sum=self.n1+self.n2+self.n3
        print("Sum is",sum)
myc=cal1()
myc.selfdata(3,4,5)
myc.declare()
