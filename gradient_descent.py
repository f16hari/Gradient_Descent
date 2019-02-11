from p5 import *

data = []
m = 1
d = 0
learning_rate = 0.05


def draw():
    size(600, 600)
    background(10)

    if len(data) > 1:
        gradient_descent()

    for i in data:
        fill(255)
        stroke(255)
        x = i[0]
        y = i[1]
        x = remap(x, (0, 1), (0, 600))
        y = remap(y, (0, 1), (600, 0))
        circle((x, y), 10)


def gradient_descent():

    global m,d,learning_rate

    for i in data:
        x = i[0]
        y = i[1]

        guess = m * x + d
        error = y - guess

        m = m + (error * x) * learning_rate
        d = d + (error) * learning_rate

    x1 = 0
    x2 = 1
    y1 = (m * x1) + d
    y2 = (m * x2) + d

    x1 = remap(x1, (0, 1), (0, 600))
    x2 = remap(x2, (0, 1), (0, 600))
    y1 = remap(y1, (0, 1), (600, 0))
    y2 = remap(y2, (0, 1), (600, 0))
    print('y1 , y2 ,d',y1,y2,d)
    line((x1, y1), (x2, y2))


def mouse_pressed(event):
    x= int(event.x)
    y= int(event.y)

    x = remap(x, (0, 600), (0, 1))
    y = remap(y, (0, 600), (1, 0))

    data.append([x, y])

    gradient_descent()


if __name__ == '__main__':
    run()
