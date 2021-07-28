class Shape: 
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape): 
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length**2


question = int(input("정사각형의 한 변의 길이를 입력하세요:"))
answer = Square(question)
print('정사각형의 면적:', answer.area())