from numpy.linalg import inv
from numpy import dot
from numpy import around

a = [
[2.875, -0.125, 0.094, -0.156, -0.125, 0.125, 0.281, 0.156],
[0.094, -0.594, -0.062, 0.0, -0.219, 0.344, -0.187, 0.0],
[0.438, 0.188, 0.219, 0.094, 0.25, 0.25, -0.031, 0.719],
[-0.281, -0.219, 0.25, -0.312, 0.094, -0.344, -0.437, -0.375],
[0.188, -0.062, -0.219, 0.031, -0.062, 0.188, 0.219, -0.656],
[0.156, -0.281, -0.125, 0.188, -0.281, 0.031, 0.125, 0.063],
[0.313, -0.062, 0.219, -0.031, 0.125, -0.25, 0.219, -0.906],
[0.219, -0.344, 0.125, -0.312, 0.219, -0.344, -0.187, 0.5]
]

ainv = inv(a)
b = [
[2.734, 0.016, 0.234, -0.297, 0.016, -0.016, 0.141, 0.297],
[-0.047, -0.453, 0.078, -0.141, -0.078, 0.203, -0.328, 0.141],
[0.578, 0.047, 0.078, 0.234, 0.109, 0.391, 0.109, 0.578],
[-0.141, -0.359, 0.109, -0.172, -0.047, -0.203, -0.297, -0.516],
[0.047, 0.078, -0.078, -0.109, 0.078, 0.047, 0.078, -0.516],
[0.016, -0.141, 0.016, 0.047, -0.141, -0.109, -0.016, 0.203],
[0.453, -0.203, 0.078, 0.109, -0.016, -0.109, 0.359, -1.047],
[0.359, -0.484, -0.016, -0.172, 0.078, -0.203, -0.047, 0.359]
]

x = (dot(ainv, b))
print(dot(a, x))
print("[")
for i in range(8):
    s = ""
    s += "["
    for j in range(7):
        s += str(round(x[i][j], 3)) + ', '
    s += str(round(x[i][7], 3))
    s += ", "
    s = s[:-2]
    s += "],"
    print(s)
print("]")
