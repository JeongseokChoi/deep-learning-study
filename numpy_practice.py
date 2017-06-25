#-*- coding: utf-8 -*-


import numpy


def practice1():
    '''numpy 배열 선언'''
    
    x = numpy.array([1.0, 2.0, 3.0])
    print(x)
    print(type(x))
    
    
def practice2():
    '''numpy 배열의 산술 연산'''
    
    x = numpy.array([1.0, 2.0, 3.0])
    y = numpy.array([2.0, 4.0, 6.0])
    print(x)
    print(y)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    
    
def practice3():
    '''broadcast 예제'''
    
    A = numpy.array([[1, 2], [3, 4]])
    B = numpy.array([10, 20])
    print(A)
    print(B)
    print(A * B)
    
    
def practice4():
    '''numpy 배열 원소에 접근'''
    
    X = numpy.array([[51, 55], [14, 19], [0, 4]])
    print(X)
    print(X[0])
    print(X[0][1])
    
    X = X.flatten()
    print(X)
    print(X[numpy.array([0, 2, 4])])
    
    print(X > 15)
    print(X[X > 15])


if __name__ == '__main__':

    print(practice1.__doc__)
    practice1()

    print(practice2.__doc__)
    practice2()
    
    print(practice3.__doc__)
    practice3()
    
    print(practice4.__doc__)
    practice4()