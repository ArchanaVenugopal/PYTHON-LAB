class Time():

  def __init__(self, hours, mins, sec):
    self.hours = hours
    self.mins = mins
    self.sec= sec
  def __add__(t1, t2):
    t3 = Time(0,0,0)
    if t1.mins+t2.mins > 60:
      t3.hours = (t1.mins+t2.mins)//60
      #print(t3.hours)
    t3.hours = t3.hours+t1.hours+t2.hours
    t3.mins =(t1.mins+t2.mins)%60

    if t1.sec+t2.sec > 60:
      t3.mins=(t1.sec+t2.sec)//60+t3.mins
      #t3.mins=t3.mins+t1.mins+t2.mins
      t3.sec=(t1.sec+t2.sec)%60
    #print(t3.mins)
    return t3

  def displayTime(self):
    print("Time is ",self.hours,"hours and",self.mins,"minutes and",self.sec,"seconds.")

h1 = int(input("enter hour1:"))
m1 = int(input("enter minutes1:"))
s1 = int(input("enter second1:"))
h2 = int(input("enter hour2:"))
m2 = int(input("enter minutes2:"))
s2 = int(input("enter second2:"))

a = Time(h1, m1, s1)
b = Time(h2, m2, s2)
c = a + b

c.displayTime()

