import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data



class Function:
    def __call__(self, input):
        x = input.data
        # y = x ** 2
        y = self.forward(x) # 集体计算方法在forward中进行
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()


class Square(Function):
    def forward(self, x):
        return x ** 2


class Exp(Function):
    def forward(self, x):
        return np.exp(x);


# 数值微分实现, 或者倒数的实现
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.datta - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2*eps)

# 实现 y = (e^x^2)^2
A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

print(y.data)

