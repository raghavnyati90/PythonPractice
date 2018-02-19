class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

a.go()
print("\n")
b.go()
print("\n")
c.go()
print("\n")
d.go()
print("\n")
e.go()
print("\n")

a.stop()
print("\n")
b.stop()
print("\n")
c.stop()
print("\n")
d.stop()
print("\n")
e.stop()
print("\n")

a.pause()
print("\n")
b.pause()
print("\n")
c.pause()
print("\n")
d.pause()
print("\n")
e.pause()