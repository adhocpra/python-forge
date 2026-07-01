#if it looks like a duck and behaves a duck, it is a duck
#special in Python
class Bird:
    def fly(self):
        print("Bird is flying")
class Aeroplane:
    def fly(self):
        print("Aeroplane is flying")
b1=Bird()
a1=Aeroplane()

def do_fly(object):
    object.fly()

do_fly(b1)
do_fly(a1)

#having same method is enough doesn't care what class