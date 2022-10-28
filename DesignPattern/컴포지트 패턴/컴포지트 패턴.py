from abc import *

##component
class Node(metaclass=ABCMeta):
    def __init__(self):
        self.name

    @abstractmethod
    def print(self):
        pass

## leaf
class File(Node):
    def __init__(self,name):
        self.name = name

    def print(self):
        print(f'파일이름: {self.name}')


##composite
class Directory(Node):
    def __init__(self,name):
        self.name = name
        self.nodes = []

    def add(self,node):
        self.nodes.append(node)

    def remove(self,node):
        self.nodes.remove(node)

    def print(self):
        print(f'디렉토리 이름: {self.name}')
        for node in self.nodes:
            node.print()

directory = Directory('/')        # 루트 디렉토리 생성
directory.add(File('data1.txt'))  # File의 객체를 directory객체의 nodes리스트에 추가한다.
directory.add(File('data2.txt'))  # File의 객체를 directory객체의 nodes리스트에 추가한다.

directory2 = Directory('hello')   # 루트 디렉토리 생성
directory2.add(File('data3.txt')) # File의 객체를 directory2객체의 nodes리스트에 추가한다.
directory.add(directory2)         # directory2 객체를 directory 객체의 nodes 리스트에 추가
print('루트 디렉토리 출력')
directory.print()                 # directory객체의 nodes 리스트에 담긴 data1, data2출력되고 directory2에 대해서는 Directory클래스의
                                  # print가 출력된다.

'''
컴포지트 패턴
- 컴포지트 패턴을 통해 트리구조로 작성하여 전체 계층을 표현하는 방법
- component 타입의 부분 객체들(컴포지트와 리프)을 다룰 수 있다.
'''