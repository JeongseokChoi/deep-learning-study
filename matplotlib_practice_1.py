#-*- coding: utf-8 -*-


import numpy
import matplotlib.pyplot


# 데이터 준비
x = numpy.arange(0, 6, 0.1)  # 0에서 6까지 0.1 간격으로 생성
y = numpy.sin(x)

#그래프 그리기
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()
