class q():
    def __init__(self, m, p1=None, p2=None, p3=None):
        self.m = m
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def search(self, x):
        if self.m == x:
            return True
        elif self.p1 and self.p1.m == x :

            return True
        elif self.p2 and self.p2.m ==x:

            return True
        elif self.p3 and self.p3.m == x:

            return True
        else:
            if self.p1:
                self.p1.search(x)
            if self.p2:
                self.p2.search(x)
            if self.p3:
                self.p3.search(x)

        return False
        #

        #
        # return False

    def send_q(self):
        print('send' + self.m)


q4 = q(m="rajvendra")
q3 = q(m="whats yo name?")
q2 = q(m="you like computer?")
q1 = q(m="hiii guys")

q1.p1 = q2
q1.p2 = q3

print(q1.search(q1.m))
