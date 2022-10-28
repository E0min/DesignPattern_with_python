import random
from abc import *

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self,x,y,radius,bg_image):
        self.x = x
        self.y = y
        self.radius = radius
        self.bg_image = bg_image

    def draw(self):
        print(f'원 그리기 \n x,y: {self.x},{self.y} 반지름: {self.radius}, 배경이미지: {self.bg_image}')

## Circle 클래스는 x,y,radius,bg_image를 객체 생성시 인자를 받고 draw로 출력한다.

class Image:
    def __init__(self,filename):
        self.filename = filename
        print(f'이미지 로드 {self.filename} ')
## Image 클래스는 filename을 받아 그 이미지를 로드한다.

class ShapeFactory:
    bg_images = {} # bg_images 빈 딕셔너리 {파일이름:이미지 로드}

    @classmethod
    def get_circle(cls,x,y,radius,bg_image_filename):
        bg_image = cls.bg_images.get(bg_image_filename,None)
        # bg_images딕셔너리에 입력받은 bg_image_filename이라는 키가 없을 시 bg_name에는 None 값이 담긴다.

        if bg_image is None: # bg_images딕셔너리에 입력받은 bg_image_filename이라는 키가 존재할 경우 그 값을 반환한다.
            bg_image = Image(bg_image_filename) #bg_image_filename가 없으니 인스턴스화하여 생성후(이미지 로드)
            cls.bg_images[bg_image_filename] = bg_image
            #딕셔너리에 파일이름을 키, 객체(로드된 이미지)를 값으로 딕셔너리에 추가 만약 다음에 또 이 이미지파일을 불러온다면 새로운 객체를 만드는 것이 아닌
            #이미 딕셔너리에 저장된 객체를 반환한다. 32줄에서 bg_image에 객체반환(로드 된 이미지)
        return Circle(x, y, radius, bg_image)
        ## get_circle은 객체를 반환하는 메소드

bg_image_filenames = ['flower.jpg','butterfly.jpg']
circles = []
for i in range(2):
    x = random.randint(0,10)
    y = random.randint(0, 10)
    radius = random.randint(0,10)
    bg_image_filename = bg_image_filenames[i]

    circle = ShapeFactory.get_circle(x,y,radius,bg_image_filename)
    # bg_image_filenames가 이미 생성된 객체라면 그대로 반환, 아니면 생성후 반환 (여기가 객체공유 일어나는 지점)Circle객체 생성하여 반환
    circles.append(circle) # 객체배열에 생성된 객체 추가

for circle in circles:
    circle.draw() # 그린다.