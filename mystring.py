# class MyString

class MyString:
    def __init__(self, s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        return self.s + other

    def __radd__(self, other):
        return other + self.s

    def __mul__(self, other):
        return self.s * other

    def __neg__(self):
        return self.s[::-1]

s = MyString('Pythom Programming is Good')
t = s / ' '
print(t)

print(s + ' Job')

print("Hello" + " " + MyString("World"))

print(MyString('Python ') * 3)

print(-MyString('Python'))
