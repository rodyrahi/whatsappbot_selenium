import gc


class Car():
    def __init__(self, name=None):
        self.rate = 20
        self.speed = 200
        self.name = name





maruti = Car("maruti")

tata = Car('tata')

Benz = Car('benz')

ls=[]

for obj in gc.get_objects():
    if isinstance(obj,Car):
        print(obj.name)
        ls.append(obj)

print(ls)

