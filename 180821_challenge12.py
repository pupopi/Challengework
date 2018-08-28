#チャレンジ12

#12-1　４つの要素のあるクラス：リンゴ

class Apple:
    def __init__(self, c, w, n, s):
        self.color = c
        self.weight = w
        self.number = n
        self.sweet = s


#12-2 円の面積

import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*math.pi

circle = Circle(5)
print(circle.area())


#12-3 三角形の面積

class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def area(self):
        return (self.bottom*self.height)/2

triangle = Triangle(10, 5)
print(triangle.area())


#12-4 六角形の外周

class Hexagon:
    def __init__(self, l):
        self.length = l

    def caluculate_perimeter(self):
        return self.length*6

hexagon = Hexagon(5)
print(hexagon.caluculate_perimeter())



#チャレンジ13
# https://github.com/calthoff/tstp/tree/master/part_II/the_four_pillars_of_oop/challenges

#13-1 RectangleとSquareの外周計算

class Rectangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def calculate_perimeter(self):
        return self.height*2+self.width*2

class Square:
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return self.length*4

rectangle = Rectangle(3, 5)
print(rectangle.calculate_perimeter())

square = Square(5)
print(square.calculate_perimeter())


#13-2 Squareにchange_size追加

class Square:
    def __init__(self, l):
        self.length = l

    def change_size(self, c):
        self.change = c
        return self.length+self.change

square =Square(5)
print(square.change_size(-2))

#以下答え

class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)


#13-3 1で作った2つを継承

class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def calculate_perimeter(self):
        return self.height*2+self.width*2

class Square(Shape):
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return self.length*4
#メソッドオーバードライする
w_square.what_am_i()
w_rectangle.what_am_i()


#13-4 HorseとRiderのクラスをコンポジションで所有させる

class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name
        
mary = Rider("Maryrose")
stan = Horse("Alu", mary)
print(stan.owner.name)


#チャレンジ十四章
# https://github.com/calthoff/tstp/tree/master/part_II/more_object_oriented_programming/challenge

#14-1

class Square():

    square_list = []

    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return self.length*4

    def __init__(self, sl):
        self.sl = sl
        self.square_list.append(self)

a_square = Square(10)
b_square = Square(20)
c_square = Square(100)

print(Square.square_list) #error


#14-1 答え

class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)


#14-2 Squareからprint関数にデータ渡す

#answer

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)


#14-3 2つのパラメータを受け取る関数：同じオブジェクトならTrue, そうでなければFalse

class Same:
    def __init__(self):

#answer

def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))