#calculate Interest 
class cal3:
    P=0
    R=0
    T=0
    def __init__(self,P,R,T):
        self.P=P
        self.R=R
        self.T=T
    def callinterest(self):
        I=self.P*self.R*self.T/100
        self.I=I
    def display(self):
        print("Interest is",self.I)
myc=cal3(1000,3.75,5)
myc.callinterest()
myc.display()        