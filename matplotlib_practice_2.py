import numpy
import matplotlib.pyplot

# 데이터 준비
x = numpy.arange(0, 6, 0.1)  # 0에서 6까지 0.1 간격으로 생성
y1 = numpy.sin(x)
y2 = numpy.cos(x)

# 그래프 그리기
matplotlib.pyplot.plot(x, y1, label='sin')
matplotlib.pyplot.plot(x, y2, label='cos', linestyle='--')  # cos 함수는 점선으로 그리기
matplotlib.pyplot.xlabel('x')  # x축 이름
matplotlib.pyplot.ylabel('y')  # y축 이름
matplotlib.pyplot.title('sin & cos')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
